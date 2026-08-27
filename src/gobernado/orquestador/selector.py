from ..ontologia.brief import Brief
from ..pipelines.catalogo import obtener_pipeline
from ..pipelines.base import PipelineCerrado

def seleccionar_pipeline(brief: Brief) -> PipelineCerrado:
    mapa = {"saas": "lead_saas", "ecommerce": "lead_ecommerce", "agencia": "lead_agencia"}
    id_pipeline = mapa[brief.vertical.value.lower()]
    return obtener_pipeline(id_pipeline)
