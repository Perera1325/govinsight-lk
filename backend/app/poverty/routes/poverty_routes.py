from fastapi import APIRouter
from ..models import Household
from ..services.scoring import calculate_poverty_score, poverty_level
from ..services.recommendations import generate_recommendations

router = APIRouter()


@router.post("/analyze")
def analyze_household(data: Household):

    score = calculate_poverty_score(data)
    level = poverty_level(score)
    recommendations = generate_recommendations(data)

    return {
        "household_id": data.household_id,
        "poverty_score": score,
        "poverty_level": level,
        "recommendations": recommendations
    }