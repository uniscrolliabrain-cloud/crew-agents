from .lead_saas import PIPELINE_LEAD_SAAS
from .lead_ecommerce import PIPELINE_LEAD_ECOMMERCE
from .lead_agencia import PIPELINE_LEAD_AGENCIA

CATALOGO_PIPELINES = {
    "lead_saas": PIPELINE_LEAD_SAAS,
    "lead_ecommerce": PIPELINE_LEAD_ECOMMERCE,
    "lead_agencia": PIPELINE_LEAD_AGENCIA,
}

def obtener_pipeline(id_pipeline: str):
    pipeline = CATALOGO_PIPELINES.get(id_pipeline)
    if pipeline is None:
        raise KeyError(f"Pipeline '{id_pipeline}' no existe en el catálogo cerrado")
    return pipeline
