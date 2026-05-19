import os
import sys
import json
import time
import logging
import jsonschema
from typing import Dict, Any, Optional

# --- 1. SETUP ---
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA_PATH = os.path.join(ROOT_DIR, "schemas", "core", "capability_discovery.json")
LOG_DIR = os.path.join(ROOT_DIR, "logs")

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(LOG_DIR, "ep_osa_connector.log"), encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("EpOsaConnector")

# --- 2. DISCOVERY & VALIDATION (THE BORDER CONTROLLER) ---
class DynamicDiscoveryController:
    """Handles the Service Discovery via Agent Introspection pattern."""
    
    def __init__(self):
        self.schema = self._load_schema()
        
    def _load_schema(self) -> dict:
        try:
            with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load core discovery schema: {e}")
            return {}

    def validate_and_load(self, payload: Dict[str, Any]) -> bool:
        """Strictly validates incoming agent capabilities against the core schema."""
        if not self.schema:
            logger.error("Validation failed: Schema not loaded.")
            return False
            
        try:
            jsonschema.validate(instance=payload, schema=self.schema)
            # Constitutional Check
            identity = payload.get("agent_identity", {})
            if not identity.get("constitutional_compliance_flag", False):
                logger.error(f"Validation failed: Agent {identity.get('name')} rejected. Constitutional compliance flag is false or missing.")
                return False
                
            logger.info(f"✅ Agent '{identity.get('name')} v{identity.get('version')}' successfully validated.")
            return True
        except jsonschema.exceptions.ValidationError as e:
            logger.error(f"Validation failed: Invalid schema format. Reason: {e.message}")
            return False


# --- 3. CORE ORCHESTRATOR ---
class EvoOsaCore:
    """Thin orchestrator acting as the 'Puck' navigating the 'Board'."""
    
    def __init__(self, session_id: str = "PEAR_OSA_1"):
        self.session_id = session_id
        self.status = "INITIALIZED"
        self.discovery_controller = DynamicDiscoveryController()
        
        # Memory Layer 1 (Session Context - 60% rule)
        self.active_skills: Dict[str, Any] = {}
        self.logs = []
        
        logger.info(f"🚀 EP-OSA Core Connector '{self.session_id}' activated.")

    def log_action(self, action: str, details: str):
        self.logs.append({"time": time.strftime("%H:%M:%S"), "action": action, "details": details})
        logger.info(f"[{action}] {details}")

    def discover_agent(self, mock_json_path: str):
        """Simulates querying an external agent for its capabilities."""
        self.log_action("discover", f"Querying external agent at {mock_json_path}...")
        
        if not os.path.exists(mock_json_path):
            self.log_action("error", "Mock payload file not found.")
            return
            
        try:
            with open(mock_json_path, "r", encoding="utf-8") as f:
                payload = json.load(f)
                
            if self.discovery_controller.validate_and_load(payload):
                agent_name = payload["agent_identity"]["name"]
                self.active_skills[agent_name] = payload["capabilities"]
                self.log_action("discovery_success", f"Loaded {len(payload['capabilities'])} skills from {agent_name}.")
            else:
                self.log_action("discovery_rejected", "Agent payload failed Border Control validation.")
                
        except Exception as e:
            self.log_action("error", f"Failed to read payload: {e}")

    def broadcast_message(self, target: str, message: str):
        """Routes a broadcast message to connected skills matching the target."""
        self.log_action("broadcast", f"Target: {target} | Msg: {message}")
        
        payload = {
            "type": "broadcast",
            "target": target.split(","),
            "action": "notify",
            "message": message,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        
        # Simulate dispatching to active skills
        dispatched_count = 0
        for agent_name, skills in self.active_skills.items():
            if "all" in payload["target"] or any(t.strip() == agent_name for t in payload["target"]):
                self.log_action("dispatch", f"-> Sent to {agent_name}")
                dispatched_count += 1
                
        if dispatched_count == 0:
            print("⚠️ Broadcast not dispatched: no matching agents found.")
        else:
            print(f"✅ Broadcast dispatched to {dispatched_count} agents.\nPayload: {json.dumps(payload, indent=2)}")

    def display_status(self):
        print(f"\n--- 👑 EP-OSA CORE STATUS ({self.session_id}) ---")
        print(f"State: {self.status}")
        print(f"Memory Layer 1 (Active Skills):")
        if not self.active_skills:
            print("  - No external skills loaded.")
        for agent, skills in self.active_skills.items():
            print(f"  🤖 Agent: {agent}")
            for skill in skills:
                print(f"     └─ ⚡ {skill['skill_name']} ({skill.get('description', 'No description')})")
        print("--------------------------------------------------")

    def pear_shell(self):
        """Interactive CLI interface inspired by A24 PEAR Shell."""
        print("\n--- 🍐 PEAR Shell (EP-OSA Modern Architecture) ---")
        print("Type 'help' for commands.")
        
        while True:
            try:
                cmd_input = input("PEAR> ").strip()
                if not cmd_input:
                    continue
                    
                parts = cmd_input.split(" ", 1)
                cmd = parts[0].lower()
                args = parts[1] if len(parts) > 1 else ""

                if cmd == "exit":
                    self.log_action("shell_exit", "PEAR Shell terminated.")
                    print("Shutting down EP-OSA Core. Goodbye!")
                    break
                elif cmd == "status":
                    self.display_status()
                elif cmd == "discover":
                    if not args:
                        print("Usage: discover <path_to_mock_json>")
                    else:
                        self.discover_agent(args)
                elif cmd == "logs":
                    for log in self.logs[-10:]:
                        print(f"[{log['time']}] {log['action']}: {log['details']}")
                elif cmd == "broadcast":
                    if not args or " " not in args:
                        print("Usage: broadcast <target> <message>")
                    else:
                        target, msg = args.split(" ", 1)
                        self.broadcast_message(target, msg)
                elif cmd_input.startswith("#evo[PEAR:broadcast:"):
                    try:
                        target_end = cmd_input.find("]")
                        target = cmd_input[20:target_end]
                        msg = cmd_input[target_end+1:].strip()
                        self.broadcast_message(target, msg)
                    except Exception:
                        print("Invalid #evo broadcast syntax.")
                elif cmd == "help":
                    print("Commands: status, discover <path>, broadcast <target> <msg>, logs, exit")
                    print("You can also use legacy syntax: #evo[PEAR:broadcast:target] message")
                else:
                    print("Unknown command. Type 'help'.")
                    
            except KeyboardInterrupt:
                print("\nUse 'exit' to quit properly.")
            except Exception as e:
                print(f"Shell Error: {e}")

if __name__ == "__main__":
    core = EvoOsaCore()
    core.pear_shell()
