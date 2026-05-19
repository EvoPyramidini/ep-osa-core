import time
import uuid
import logging
from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional

logger = logging.getLogger("ep_osa.memory")

@dataclass
class MemoryAnchor:
    """Semantic landmark in cognitive space."""
    id:              str
    semantic_label:  str
    layer:           str           # primary | buffer | reserve
    content_summary: str
    tags:            List[str]
    created_at:      float
    evolution_value: str           # high | medium | low
    connections:     List[str] = field(default_factory=list)
    usage_count:     int = 0

    def to_dict(self) -> Dict:
        return asdict(self)

@dataclass
class MemoryEntry:
    key:        str
    value:      Any
    layer:      str
    created_at: float
    accessed_at: float
    access_count: int = 0
    tags:       List[str] = field(default_factory=list)
    anchor_id:  Optional[str] = None

    def touch(self):
        self.accessed_at = time.time()
        self.access_count += 1
        
    def to_dict(self) -> Dict:
        return asdict(self)


class EvoMemorySystem:
    """
    Constitutional memory system.
    Strict 50-60% / 30% / 10% proportions.
    """

    PRIMARY_CAPACITY = 600
    BUFFER_CAPACITY  = 300
    RESERVE_CAPACITY = 100

    def __init__(self, session_id: str):
        self.session_id = session_id
        self._primary: Dict[str, MemoryEntry] = {}
        self._buffer:  Dict[str, MemoryEntry] = {}
        self._reserve: Dict[str, MemoryEntry] = {}
        self._anchors: Dict[str, MemoryAnchor] = {}
        self._tag_index: Dict[str, List[str]] = {}

    def store(self, key: str, value: Any, layer: str = "primary", tags: List[str] = None, anchor_id: str = None) -> str:
        store = self._get_store(layer)
        if len(store) >= self._capacity(layer):
            self._evict(store)

        entry = MemoryEntry(
            key=key, value=value, layer=layer,
            created_at=time.time(), accessed_at=time.time(),
            tags=tags or [], anchor_id=anchor_id
        )
        store[key] = entry

        for tag in (tags or []):
            self._tag_index.setdefault(tag, [])
            if key not in self._tag_index[tag]:
                self._tag_index[tag].append(key)
        return key

    def retrieve(self, key: str, layer: str = "primary") -> Optional[Any]:
        store = self._get_store(layer)
        entry = store.get(key)
        if entry:
            entry.touch()
            return entry.value
        return None

    def search_by_tags(self, tags: List[str]) -> List[Dict]:
        matching_keys = set()
        for tag in tags:
            for key in self._tag_index.get(tag, []):
                if not key.startswith("anchor:"):
                    matching_keys.add(key)
                    
        results = []
        for key in matching_keys:
            for layer in ("primary", "buffer", "reserve"):
                entry = self._get_store(layer).get(key)
                if entry:
                    results.append(entry.to_dict())
                    break
        return results

    def quantum_jump(self, from_anchor_id: str, to_anchor_id: str, carry_keys: List[str] = None) -> Dict:
        src = self._anchors.get(from_anchor_id)
        dst = self._anchors.get(to_anchor_id)
        if not src or not dst:
            return {"status": "error", "reason": "anchor_not_found"}

        carried = {}
        for key in (carry_keys or []):
            for layer in ("primary", "buffer", "reserve"):
                val = self.retrieve(key, layer)
                if val is not None:
                    carried[key] = val
                    self.store(key, val, layer=dst.layer, tags=dst.tags)
                    break

        if to_anchor_id not in src.connections:
            src.connections.append(to_anchor_id)

        return {
            "status": "success",
            "from":   src.semantic_label,
            "to":     dst.semantic_label,
            "carried_keys": list(carried.keys()),
            "is_quantum_leap": True,
        }

    def _get_store(self, layer: str) -> Dict[str, MemoryEntry]:
        return {"primary": self._primary, "buffer": self._buffer, "reserve": self._reserve}.get(layer, self._primary)

    def _capacity(self, layer: str) -> int:
        return {"primary": self.PRIMARY_CAPACITY, "buffer": self.BUFFER_CAPACITY, "reserve": self.RESERVE_CAPACITY}.get(layer, self.PRIMARY_CAPACITY)

    def _evict(self, store: Dict[str, MemoryEntry]):
        if not store: return
        lru_key = min(store, key=lambda k: store[k].accessed_at)
        del store[lru_key]


# --- SKILL EXECUTOR ADAPTER ---

# In a real environment, this system instance would be persisted or passed from the orchestrator.
# For the stateless adapter, we simulate a global memory instance for the current run.
_GLOBAL_MEMORY = EvoMemorySystem(session_id="default_session")

def execute(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Entry point conforming to contract.yaml for ep-osa-memory.
    """
    action = payload.get("action")
    
    if action == "create_container":
        container_type = payload.get("container_type", "unknown")
        content = payload.get("content", {})
        
        container_id = f"cont_{uuid.uuid4().hex[:8]}"
        tags = [container_type]
        if isinstance(content, dict) and "tags" in content:
            tags.extend(content["tags"])
            
        _GLOBAL_MEMORY.store(key=container_id, value=content, layer="primary", tags=tags)
        
        return {
            "status": "success",
            "container_id": container_id,
            "is_quantum_leap": False
        }
        
    elif action == "extract_context":
        query = payload.get("query", "")
        # Very simplified keyword matching into tags
        tags_to_search = [word.lower() for word in query.split() if len(word) > 3]
        if not tags_to_search:
            tags_to_search = ["thought", "log", "session"]
            
        context = _GLOBAL_MEMORY.search_by_tags(tags_to_search)
        
        # Simulating Quantum Leap randomly if requested probability is met
        import random
        probability = payload.get("quantum_leap_probability", 0.0)
        is_leap = random.random() < probability
        
        if is_leap and len(_GLOBAL_MEMORY._anchors) >= 2:
            # We don't have enough anchors to do a real jump, but we simulate the flag
            pass
            
        return {
            "status": "success",
            "context": context,
            "is_quantum_leap": is_leap
        }
        
    elif action == "trigger_quantum_leap":
        # Force a quantum leap
        anchors = list(_GLOBAL_MEMORY._anchors.keys())
        if len(anchors) < 2:
            return {
                "status": "error",
                "error_message": "Not enough semantic anchors to perform a quantum leap."
            }
        
        import random
        src = random.choice(anchors)
        dst = random.choice([a for a in anchors if a != src])
        
        result = _GLOBAL_MEMORY.quantum_jump(src, dst)
        return {
            "status": "success" if result["status"] == "success" else "error",
            "context": [{"quantum_jump_result": result}],
            "is_quantum_leap": True
        }
        
    elif action == "broadcast_receive":
        msg = payload.get("broadcast_message", {})
        # Store broadcast message in buffer memory
        msg_id = f"bcast_{uuid.uuid4().hex[:8]}"
        _GLOBAL_MEMORY.store(key=msg_id, value=msg, layer="buffer", tags=["broadcast"])
        
        return {
            "status": "success",
            "container_id": msg_id,
            "is_quantum_leap": False
        }
        
    else:
        return {
            "status": "error",
            "error_message": f"Unknown action: {action}"
        }

if __name__ == "__main__":
    # Test execution
    print(execute({
        "action": "create_container",
        "container_type": "thought",
        "content": {"idea": "Implement PEAR routing", "tags": ["routing", "pear"]}
    }))
