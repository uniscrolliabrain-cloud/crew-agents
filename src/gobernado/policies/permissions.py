# policies/permissions.py
from pydantic import BaseModel

class PermissionsPolicy(BaseModel):
    allowed_tools: list[str] = ["search", "validate_email"]
