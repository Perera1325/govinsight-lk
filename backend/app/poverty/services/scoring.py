def calculate_poverty_score(data):
    score = 0

    # Income factor
    if data.monthly_income < 20000:
        score += 30
    elif data.monthly_income < 40000:
        score += 20
    else:
        score += 5

    # Housing
    if data.housing_condition == 1:
        score += 25
    elif data.housing_condition == 2:
        score += 15

    # Sanitation
    if data.sanitation == 0:
        score += 20
    elif data.sanitation == 1:
        score += 10

    # Education
    if data.education_access == 0:
        score += 15
    elif data.education_access == 1:
        score += 8

    # Health risk
    if data.health_risk == 2:
        score += 10
    elif data.health_risk == 1:
        score += 5

    return score


def poverty_level(score):
    if score >= 70:
        return "High Poverty Risk"
    elif score >= 40:
        return "Medium Poverty Risk"
    else:
        return "Low Poverty Risk"