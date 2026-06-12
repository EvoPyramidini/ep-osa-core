from typing import Any, Dict, Optional
from pydantic import BaseModel, Field

class BaseEnvironment(BaseModel):
    """
    Abstract representation of an external execution environment (e.g., another EvoPyramid project).
    This serves as the root class for the 'environments' module.
    """
    env_id: str = Field(..., description="Unique identifier for the environment")
    root_path: Optional[str] = Field(default=None, description="Absolute or relative path to the environment's root directory")
    is_active: bool = Field(default=True, description="Whether this environment is currently active and reachable")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Custom metadata about the environment")

    def connect(self) -> bool:
        """
        Establish a connection or verify access to the environment.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement 'connect'")

    def execute_action(self, action_name: str, payload: Dict[str, Any]) -> Any:
        """
        Execute an action within this specific environment.
        """
        raise NotImplementedError("Subclasses must implement 'execute_action'")
