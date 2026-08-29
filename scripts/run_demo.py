import sys
from pathlib import Path

# Añade src/ al path para que Python encuentre el paquete gobernado
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from dotenv import load_dotenv
load_dotenv()

from gobernado.ontologia.brief import Brief
from gobernado.ontologia.vertical import Vertical
from gobernado.orquestador.selector import seleccionar_pipeline
from gobernado.execution.crewai.adapter import CrewAIBackend

brief = Brief(
    objetivo="encontrar leads SaaS B2B en fintech con equipos de 10-50 personas",
    vertical=Vertical.SAAS,
    presupuesto_max=50,
)
pipeline = seleccionar_pipeline(brief)
backend = CrewAIBackend()
resultado = backend.ejecutar_pipeline(pipeline, brief)

print("--- RESULTADO ---")
print(resultado.model_dump_json(indent=2))
if resultado.output is not None:
    print("--- LEAD COMPLETO? ---")
    print(resultado.output.esta_completo())
