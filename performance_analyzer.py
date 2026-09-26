# performance_analyzer.py

def analyze_marks(subjects, marks):
    """
    Finds the lowest marks and identifies all subjects
    having the lowest marks.
    """

    lowest_marks = min(marks)

    weak_subjects = []

    for i in range(len(subjects)):
        if marks[i] == lowest_marks:
            weak_subjects.append(subjects[i])

    return lowest_marks, weak_subjects


def analyze_attendance(subjects, attendance):
    """
    Identifies subjects having attendance below 75%.
    """

    low_attendance_subjects = []

    for i in range(len(subjects)):
        if attendance[i] < 75:
            low_attendance_subjects.append(subjects[i])

    return low_attendance_subjects


def analyze_performance(subjects, marks, attendance):
    """
    Performs complete basic academic performance analysis.
    """

    lowest_marks, weak_subjects = analyze_marks(subjects, marks)

    low_attendance_subjects = analyze_attendance(
        subjects,
        attendance
    )

    return {
        "lowest_marks": lowest_marks,
        "weak_subjects": weak_subjects,
        "low_attendance_subjects": low_attendance_subjects
    }