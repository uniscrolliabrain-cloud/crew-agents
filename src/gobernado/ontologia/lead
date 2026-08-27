from pydantic import BaseModel, Field, ConfigDict, EmailStr
from enum import Enum
from .vertical import Vertical, CompanySize

class EmailStatus(str, Enum):
    VALID = "valid"
    INVALID = "invalid"
    UNKNOWN = "unknown"

class LeadSource(str, Enum):
    LINKEDIN = "linkedin"
    WEB = "web"
    DB = "db"

class LeadTaxonomizado(BaseModel):
    model_config = ConfigDict(frozen=True)
    company_name: str = Field(min_length=2)
    vertical: Vertical
    source: LeadSource
    company_size: CompanySize | None = None  # lo rellena ENRIQUECER, no BUSCAR
    email: EmailStr | None = None
    email_status: EmailStatus = EmailStatus.UNKNOWN
    web: str | None = None

    def esta_completo(self) -> bool:
        """Chequeo de negocio: un lead listo para entregar, no solo un JSON válido."""
        return self.company_size is not None and self.email_status != EmailStatus.UNKNOWN
