# policies/execution.py
from pydantic import BaseModel

class ExecutionPolicy(BaseModel):
    max_concurrent_pipelines: int = 1
