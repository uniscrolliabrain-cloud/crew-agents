# policies/budgets.py
from pydantic import BaseModel
class BudgetPolicy(BaseModel):
    max_usd_per_brief: float = 0.0
