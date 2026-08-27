from pydantic import ValidationError

class KernelValidador:
    def validar_brief(self, brief):
        if "ilegal" in brief.objetivo.lower():
            raise ValueError("Objetivo prohibido por policy")
        return True

    def validar_transicion(self, output_model, expected_model_cls):
        try:
            expected_model_cls.model_validate(output_model.model_dump())
            return True
        except ValidationError as e:
            raise e
