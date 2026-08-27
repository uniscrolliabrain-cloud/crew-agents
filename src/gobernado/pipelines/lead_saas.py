from ..ontologia.brief import Brief
from ..ontologia.lead import LeadTaxonomizado
from .base import PipelineCerrado, PipelineStep, StepType

PIPELINE_LEAD_SAAS = PipelineCerrado(
    id="lead_saas",
    descripcion="SAAS España: buscar -> validar_email -> clasificar -> enriquecer",
    pasos=[
        PipelineStep(
            tipo=StepType.BUSCAR,
            prompt_template="Paso=buscar Vertical=SAAS Pais={pais} Objetivo={objetivo} Devuelve LeadTaxonomizado con company_name, vertical y source (no inventes company_size ni email)",
            agent_rol="buscador",
            input_schema=Brief,
            output_schema=LeadTaxonomizado,
        ),
        PipelineStep(
            tipo=StepType.VALIDAR_EMAIL,
            prompt_template="Paso=validar_email Input={input_json} Verifica MX y formato. Devuelve el mismo lead con email_status actualizado",
            agent_rol="validador",
            max_tokens=150,
            input_schema=LeadTaxonomizado,
            output_schema=LeadTaxonomizado,
        ),
        PipelineStep(
            tipo=StepType.CLASIFICAR_VERTICAL,
            prompt_template="Paso=clasificar_vertical Input={input_json} Solo permite SAAS/ECOMMERCE/AGENCIA, confirma o corrige el campo vertical",
            agent_rol="validador",
            max_tokens=100,
            input_schema=LeadTaxonomizado,
            output_schema=LeadTaxonomizado,
        ),
        PipelineStep(
            tipo=StepType.ENRIQUECER,
            prompt_template="Paso=enriquecer Input={input_json} Añade company_size estimado en base a company_name y web",
            agent_rol="enriquecedor",
            input_schema=LeadTaxonomizado,
            output_schema=LeadTaxonomizado,
        ),
    ]
)
