from fastapi import APIRouter
from ..models import Household
from ..services.scoring import calculate_poverty_score, poverty_level

router = APIRouter()


@router.post("/analyze")
def analyze_household(data: Household):

    score = calculate_poverty_score(data)
    level = poverty_level(score)

    return {
        "household_id": data.household_id,
        "poverty_score": score,
        "poverty_level": level
    }