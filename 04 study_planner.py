# ==========================================================
# STUDYMATE AI - STUDY PLANNER
# ==========================================================


def get_study_hours(marks):

    if marks < 40:
        return 3

    elif marks < 50:
        return 2

    elif marks < 60:
        return 1.5

    else:
        return 1


def create_study_plan(subject, marks):

    hours = get_study_hours(marks)

    if marks < 40:
        task = "Revise weak topics and solve practice questions."

    elif marks < 50:
        task = "Practice important questions and revise concepts."

    elif marks < 60:
        task = "Revise concepts and solve some practice questions."

    else:
        task = "Regular revision and practice."

    return {
        "subject": subject,
        "study_hours": hours,
        "task": task
    }


def generate_daily_plan(
    subject1, marks1,
    subject2, marks2,
    subject3, marks3,
    subject4, marks4
):

    plan1 = create_study_plan(subject1, marks1)
    plan2 = create_study_plan(subject2, marks2)
    plan3 = create_study_plan(subject3, marks3)
    plan4 = create_study_plan(subject4, marks4)

    return [plan1, plan2, plan3, plan4]


def display_study_plan(plans):

    print("\n---------- PERSONALIZED STUDY PLAN ----------")

    total_hours = 0

    for plan in plans:

        print("\nSubject:", plan["subject"])
        print("Study Time:", plan["study_hours"], "hours/day")
        print("Task:", plan["task"])

        total_hours = total_hours + plan["study_hours"]

    print("\nTotal Recommended Study Time:",
          total_hours,
          "hours/day")


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    plans = generate_daily_plan(
        "Mathematics", 95,
        "Python", 75,
        "EVS", 98,
        "Communication", 55
    )

    display_study_plan(plans)
