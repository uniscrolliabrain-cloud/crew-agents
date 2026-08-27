from pydantic import BaseModel, Field, ConfigDict
from .vertical import Vertical

class Brief(BaseModel):
    model_config = ConfigDict(frozen=True)
    objetivo: str = Field(min_length=10, max_length=500)
    vertical: Vertical
    pais: str = Field(default="ES", pattern=r"^[A-Z]{2}$")
    presupuesto_max: int = Field(ge=0, le=100000)
    emails_permitidos: list[str] = Field(default_factory=lambda: [".com", ".es"])
    prohibiciones: list[str] = Field(default_factory=list)
