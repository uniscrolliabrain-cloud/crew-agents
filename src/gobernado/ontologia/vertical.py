from enum import Enum

class Vertical(str, Enum):
    SAAS = "SAAS"
    ECOMMERCE = "ECOMMERCE"
    AGENCIA = "AGENCIA"

class CompanySize(str, Enum):
    S_1_10 = "1-10"
    S_11_50 = "11-50"
    S_51_200 = "51-200"
    S_200_PLUS = "200+"
