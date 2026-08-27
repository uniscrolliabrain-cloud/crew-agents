from ..ontologia.brief import Brief
from ..ontologia.lead import LeadTaxonomizado
from .base import PipelineCerrado, PipelineStep, StepType

PIPELINE_LEAD_AGENCIA = PipelineCerrado(
    id="lead_agencia",
    descripcion="Pipeline AGENCIA: buscar -> validar_email",
    pasos=[
        PipelineStep(
            tipo=StepType.BUSCAR,
            prompt_template="Paso=buscar Vertical=AGENCIA Pais={pais} Objetivo={objetivo} Devuelve LeadTaxonomizado con company_name, vertical y source",
            agent_rol="buscador",
            input_schema=Brief,
            output_schema=LeadTaxonomizado,
        ),
        PipelineStep(
            tipo=StepType.VALIDAR_EMAIL,
            prompt_template="Paso=validar_email Input={input_json} Verifica MX y formato",
            agent_rol="validador",
            input_schema=LeadTaxonomizado,
            output_schema=LeadTaxonomizado,
        ),
    ]
)
