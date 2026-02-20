def generate_recommendations(data):

    recommendations = []

    # Housing
    if data.housing_condition == 1:
        recommendations.append("Eligible for housing repair or subsidy program")

    # Sanitation
    if data.sanitation == 0:
        recommendations.append("Priority for sanitation/toilet development assistance")

    # Education
    if data.education_access == 0:
        recommendations.append("Children eligible for education support or scholarships")

    # Income
    if data.monthly_income < 20000:
        recommendations.append("Financial aid or livelihood development support required")

    # Health
    if data.health_risk == 2:
        recommendations.append("Health intervention and medical support recommended")

    return recommendations