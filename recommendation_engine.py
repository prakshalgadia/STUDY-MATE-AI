# ==========================================================
# STUDYMATE AI - RECOMMENDATION ENGINE
# ==========================================================


def get_priority(marks, attendance, days):

    if marks < 40 and attendance < 75 and days <= 7:
        return "HIGH PRIORITY"

    elif marks < 40 or attendance < 75 or days <= 7:
        return "MEDIUM PRIORITY"

    else:
        return "LOW PRIORITY"


def get_reason(marks, attendance, days):

    reasons = []

    if marks < 60:
        reasons.append("Low Marks")

    if attendance < 75:
        reasons.append("Low Attendance")

    if days <= 7:
        reasons.append("Exam Near")

    if len(reasons) == 0:
        return "No Major Concern"

    return " + ".join(reasons)


def get_recommendation(marks, attendance, days):

    if marks < 40 and attendance < 75 and days <= 7:
        return "Focus immediately. Revise important topics and practice questions."

    elif marks < 40:
        return "Marks are low. Give extra time to this subject and practice more questions."

    elif attendance < 75:
        return "Attendance is below 75%. Attend classes regularly and revise missed topics."

    elif days <= 7:
        return "Exam is near. Focus on important topics and quick revision."

    elif marks < 60:
        return "Improve your concepts and practice more questions."

    else:
        return "Continue regular study and revision."


def generate_recommendation(subject, marks, attendance, days):

    priority = get_priority(marks, attendance, days)

    reason = get_reason(marks, attendance, days)

    recommendation = get_recommendation(
        marks,
        attendance,
        days
    )

    return {
        "subject": subject,
        "priority": priority,
        "reason": reason,
        "recommendation": recommendation
    }


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    result = generate_recommendation(
        "Mathematics",
        95,
        70,
        5
    )

    print("\n---------- RECOMMENDATION ENGINE TEST ----------")

    print("Subject:", result["subject"])
    print("Priority:", result["priority"])
    print("Reason:", result["reason"])
    print("Recommendation:", result["recommendation"])