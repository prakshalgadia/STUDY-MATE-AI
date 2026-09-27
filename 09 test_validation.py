import unittest
from validation import validate_marks, validate_attendance, validate_subject_name, validate_student_name

class TestValidation(unittest.TestCase):
    def test_valid_marks(self):
        self.assertTrue(validate_marks(80))
    def test_invalid_marks(self):
        self.assertFalse(validate_marks(120))
    def test_valid_attendance(self):
        self.assertTrue(validate_attendance(75))
    def test_invalid_attendance(self):
        self.assertFalse(validate_attendance(-5))
    def test_subject_name(self):
        self.assertTrue(validate_subject_name("Python"))
        self.assertFalse(validate_subject_name(""))
    def test_student_name(self):
        self.assertTrue(validate_student_name("Student"))
        self.assertFalse(validate_student_name(""))

if __name__ == "__main__":
    unittest.main()
