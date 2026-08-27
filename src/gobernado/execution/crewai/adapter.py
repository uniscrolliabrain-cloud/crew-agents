from crewai import Agent, Task, Crew
from pydantic import ValidationError, BaseModel
from ...pipelines.base import PipelineStep, PipelineCerrado
from ...ontologia.brief import Brief
from ..interface import ExecutionResult, ErrorTipo
from ...kernel.reintento import KernelReintento, IntentoState
from ...kernel.validador import KernelValidador

class CrewAIBackend:
    def _clasificar_error(self, paso: PipelineStep, e: Exception) -> ExecutionResult:
        mensaje = str(e).lower()
        if "429" in mensaje or "rate limit" in mensaje or "resource_exhausted" in mensaje:
            tipo = ErrorTipo.RATE_LIMIT
        elif "timeout" in mensaje:
            tipo = ErrorTipo.TIMEOUT
        elif "validation" in mensaje or "pydantic" in mensaje:
            tipo = ErrorTipo.SCHEMA_INVALIDO
        else:
            tipo = ErrorTipo.LLM_ERROR
        return ExecutionResult(paso_fallido=paso, error_tipo=tipo, error_detalle=str(e))

    def ejecutar_paso(self, paso: PipelineStep, input_data: BaseModel) -> ExecutionResult[BaseModel]:
        try:
            paso.input_schema.model_validate(input_data.model_dump())
        except ValidationError as e:
            return ExecutionResult(paso_fallido=paso, error_tipo=ErrorTipo.SCHEMA_INVALIDO, error_detalle=str(e))

        format_kwargs = {**input_data.model_dump(mode="json"), "input_json": input_data.model_dump_json()}
        agente = Agent(role=paso.agent_rol, goal=paso.prompt_template, backstory="", verbose=False)
        tarea = Task(
            description=paso.prompt_template.format(**format_kwargs),
            expected_output=str(paso.output_schema.model_json_schema()),
            agent=agente,
            output_pydantic=paso.output_schema,
        )
        try:
            resultado = Crew(agents=[agente], tasks=[tarea]).kickoff()
            if resultado.pydantic is None:
                return ExecutionResult(paso_fallido=paso, error_tipo=ErrorTipo.SCHEMA_INVALIDO, error_detalle="CrewAI no pudo estructurar el output")
            return ExecutionResult(output=resultado.pydantic)
        except Exception as e:
            return self._clasificar_error(paso, e)

    def ejecutar_pipeline(self, pipeline: PipelineCerrado, brief: Brief) -> ExecutionResult:
        validador = KernelValidador()
        try:
            validador.validar_brief(brief)
        except Exception as e:
            return ExecutionResult(paso_fallido=None, error_tipo=ErrorTipo.POLICY_VIOLATION, error_detalle=str(e))

        kernel_reintento = KernelReintento()
        dato_actual: BaseModel = brief
        for paso in pipeline.pasos:
            state = IntentoState(intento=0, max_retries=paso.max_retries)
            while True:
                resultado = self.ejecutar_paso(paso, dato_actual)
                if resultado.error_tipo is None:
                    dato_actual = resultado.output
                    break
                reintentar, state = kernel_reintento.decidir(resultado, state)
                if not reintentar:
                    return resultado
        return ExecutionResult(output=dato_actual)
