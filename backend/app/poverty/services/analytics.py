def community_summary(households):

    total = len(households)
    high = 0
    medium = 0
    low = 0

    for h in households:
        score = h["score"]

        if score >= 70:
            high += 1
        elif score >= 40:
            medium += 1
        else:
            low += 1

    return {
        "total_households": total,
        "high_poverty": high,
        "medium_poverty": medium,
        "low_poverty": low
    }