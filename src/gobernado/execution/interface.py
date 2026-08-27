from typing import Protocol, runtime_checkable, Generic, TypeVar
from enum import Enum
from pydantic import BaseModel, ConfigDict
from ..pipelines.base import PipelineStep, PipelineCerrado
from ..ontologia.brief import Brief

T = TypeVar("T", bound=BaseModel)

class ErrorTipo(str, Enum):
    SCHEMA_INVALIDO = "schema_invalido"
    TIMEOUT = "timeout"
    RATE_LIMIT = "rate_limit"
    LLM_ERROR = "llm_error"
    POLICY_VIOLATION = "policy_violation"

class ExecutionResult(BaseModel, Generic[T]):
    model_config = ConfigDict(frozen=True, arbitrary_types_allowed=True)
    output: T | None = None
    paso_fallido: PipelineStep | None = None
    error_tipo: ErrorTipo | None = None
    error_detalle: str | None = None

@runtime_checkable
class ExecutionBackend(Protocol[T]):
    def ejecutar_pipeline(self, pipeline: PipelineCerrado, brief: Brief) -> ExecutionResult[T]: ...
    def ejecutar_paso(self, paso: PipelineStep, input_data: BaseModel) -> ExecutionResult[BaseModel]: ...
