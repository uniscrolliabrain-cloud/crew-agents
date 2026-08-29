"""
crew-ai-gobernado: Capa de gobernanza sobre CrewAI para generar leads B2B.

Arquitectura:
- ontologia/: Modelos Pydantic puros (Brief, LeadTaxonomizado, Vertical, etc.)
- pipelines/: Definición de pipelines cerrados (PipelineStep, PipelineCerrado)
- kernel/: Lógica de reintentos y validación (KernelReintento, KernelValidador)
- policies/: Políticas de gobernanza (budgets, execution, permissions)
- orquestador/: Selección de pipelines
- execution/: Backends de ejecución (interface + crewai/adapter)

Solo execution/crewai/ importa crewai. El resto es Pydantic puro.
"""

__version__ = "0.1.0"
