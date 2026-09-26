import unittest
from performance_analyzer import analyze_marks, analyze_attendance

class TestPerformanceAnalyzer(unittest.TestCase):
    def test_lowest_marks(self):
        subjects = ["Maths", "Python", "Physics", "Communication"]
        marks = [40, 70, 40, 80]
        lowest, weak = analyze_marks(subjects, marks)
        self.assertEqual(lowest, 40)
        self.assertEqual(weak, ["Maths", "Physics"])

    def test_low_attendance(self):
        subjects = ["Maths", "Python", "Physics", "Communication"]
        attendance = [80, 72, 68, 85]
        result = analyze_attendance(subjects, attendance)
        self.assertEqual(result, ["Python", "Physics"])

if __name__ == "__main__":
    unittest.main()
