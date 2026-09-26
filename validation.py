# validation.py


def validate_marks(marks):
    """
    Checks whether marks are between 0 and 100.
    """

    if not isinstance(marks, (int, float)):
        return False

    if marks < 0 or marks > 100:
        return False

    return True


def validate_attendance(attendance):
    """
    Checks whether attendance is between 0 and 100.
    """

    if not isinstance(attendance, (int, float)):
        return False

    if attendance < 0 or attendance > 100:
        return False

    return True


def validate_subject_name(subject):
    """
    Checks whether subject name is not empty.
    """

    if not isinstance(subject, str):
        return False

    if subject.strip() == "":
        return False

    return True


def validate_student_name(name):
    """
    Checks whether student name is not empty.
    """

    if not isinstance(name, str):
        return False

    if name.strip() == "":
        return False

    return True