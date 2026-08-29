from pydantic import BaseModel, Field, ConfigDict
from enum import Enum
from typing import Literal, Type

class StepType(str, Enum):
    BUSCAR = "buscar"
    VALIDAR_EMAIL = "validar_email"
    CLASIFICAR_VERTICAL = "clasificar_vertical"
    ENRIQUECER = "enriquecer"
    VALIDAR_WEB = "validar_web"

class PipelineStep(BaseModel):
    model_config = ConfigDict(frozen=True, arbitrary_types_allowed=True)
    tipo: StepType
    prompt_template: str = Field(max_length=400, description="~200 tokens max")
    max_tokens: int = Field(default=200, le=300)
    max_retries: int = Field(default=3, le=5)
    agent_rol: Literal["buscador", "validador", "enriquecedor"]
    input_schema: Type[BaseModel] = Field(exclude=True)
    output_schema: Type[BaseModel] = Field(exclude=True)

class PipelineCerrado(BaseModel):
    model_config = ConfigDict(frozen=True, arbitrary_types_allowed=True)
    id: Literal["lead_saas", "lead_ecommerce", "lead_agencia"]
    descripcion: str
    pasos: list[PipelineStep] = Field(min_length=1)
