from pydantic import BaseModel


class Household(BaseModel):
    household_id: int
    monthly_income: float
    family_size: int
    housing_condition: int  # 1=poor, 2=average, 3=good
    sanitation: int         # 0=no toilet, 1=basic, 2=good
    education_access: int   # 0=poor, 1=average, 2=good
    health_risk: int        # 0=low, 1=medium, 2=high