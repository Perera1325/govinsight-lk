from fastapi import APIRouter
from typing import List

from ..models import Household
from ..services.scoring import calculate_poverty_score, poverty_level
from ..services.recommendations import generate_recommendations
from ..services.analytics import community_summary

router = APIRouter()


# -----------------------------
# Single Household Analysis
# -----------------------------
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


# -----------------------------
# Community Analysis
# -----------------------------
@router.post("/community")
def analyze_community(data: List[Household]):

    results = []

    for item in data:
        score = calculate_poverty_score(item)
        level = poverty_level(score)

        results.append({
            "household_id": item.household_id,
            "score": score,
            "level": level
        })

    summary = community_summary(results)

    return {
        "summary": summary,
        "details": results
    }