import time
import re
from pydantic import BaseModel
from ..execution.interface import ExecutionResult, ErrorTipo

class IntentoState(BaseModel):
    intento: int = 0
    max_retries: int
    def agotado(self) -> bool:
        return self.intento >= self.max_retries

class KernelReintento:
    def _parse_retry_after(self, error_detalle: str | None) -> int | None:
        if not error_detalle:
            return None
        m = re.search(r"retry-after\D*(\d+)", error_detalle, re.I)
        return int(m.group(1)) if m else None

    def _sleep_backoff(self, intento: int, error_detalle: str | None):
        retry_after = self._parse_retry_after(error_detalle)
        time.sleep(retry_after if retry_after else min(2 ** intento, 60))

    def decidir(self, result: ExecutionResult, state: IntentoState):
        if result.error_tipo is None:
            return False, state
        if state.agotado():
            return False, state
        if result.error_tipo in (ErrorTipo.RATE_LIMIT, ErrorTipo.TIMEOUT):
            self._sleep_backoff(state.intento, result.error_detalle)
            return True, IntentoState(intento=state.intento + 1, max_retries=state.max_retries)
        if result.error_tipo == ErrorTipo.SCHEMA_INVALIDO:
            return True, IntentoState(intento=state.intento + 1, max_retries=state.max_retries)
        return False, state
