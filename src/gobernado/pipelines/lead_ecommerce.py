from ..ontologia.brief import Brief
from ..ontologia.lead import LeadTaxonomizado
from .base import PipelineCerrado, PipelineStep, StepType

PIPELINE_LEAD_ECOMMERCE = PipelineCerrado(
    id="lead_ecommerce",
    descripcion="Pipeline ECOMMERCE: buscar -> validar_web",
    pasos=[
        PipelineStep(
            tipo=StepType.BUSCAR,
            prompt_template="Paso=buscar Vertical=ECOMMERCE Pais={pais} Objetivo={objetivo} Devuelve LeadTaxonomizado con company_name, vertical y source",
            agent_rol="buscador",
            input_schema=Brief,
            output_schema=LeadTaxonomizado,
        ),
        PipelineStep(
            tipo=StepType.VALIDAR_WEB,
            prompt_template="Paso=validar_web Input={input_json} Confirma que web responde 200 y coincide con company_name",
            agent_rol="validador",
            input_schema=LeadTaxonomizado,
            output_schema=LeadTaxonomizado,
        ),
    ]
)
