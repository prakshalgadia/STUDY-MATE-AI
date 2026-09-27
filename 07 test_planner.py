import unittest
from study_planner import recommend_study_hours

class TestStudyPlanner(unittest.TestCase):
    def test_low_marks(self):
        self.assertEqual(recommend_study_hours(35), 3)
    def test_medium_low_marks(self):
        self.assertEqual(recommend_study_hours(45), 2)
    def test_average_marks(self):
        self.assertEqual(recommend_study_hours(55), 1.5)
    def test_good_marks(self):
        self.assertEqual(recommend_study_hours(75), 1)

if __name__ == "__main__":
    unittest.main()
