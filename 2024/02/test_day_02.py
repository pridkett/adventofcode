import unittest
from day_02 import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_evaluate_aoc_input1(self):
        report = "7 6 4 2 1"
        s, d = self.solution.evaluate_new(report)
        self.assertEqual(s, 1)
        self.assertEqual(d, 1)

    def test_evaluate_aoc_input2(self):
        report = "1 2 7 8 9"
        s, d = self.solution.evaluate_new(report)
        self.assertEqual(s, 0)
        self.assertEqual(d, 0)

    def test_evaluate_aoc_input3(self):
        report = "9 7 6 2 1"
        s, d = self.solution.evaluate_new(report)
        self.assertEqual(s, 0)
        self.assertEqual(d, 0)

    def test_evalute_aoc_input4(self):
        report = "1 3 2 4 5"
        s, d = self.solution.evaluate_new(report)
        self.assertEqual(s, 0)
        self.assertEqual(d, 1)

    def test_evaluate_aoc_input5(self):
        report = "8 6 4 4 1"
        s, d = self.solution.evaluate_new(report)
        self.assertEqual(s, 0)
        self.assertEqual(d, 1)

    def test_evaluate_aoc_input6(self):
        report = "1 3 6 7 9"
        s, d = self.solution.evaluate_new(report)
        self.assertEqual(s, 1)
        self.assertEqual(d, 1)

    def test_evaluate_dampened_fail(self):
        reports = ["90 93 90 83 82 80 79",
                   "24 20 19 18 18 17 10",
                   "16 21 27 29 31 33 35 40"]
        results = [self.solution.evaluate_new(report) for report in reports]
        self.assertEqual(results, [(0, 0), (0, 0), (0, 0)])

    def test_evaluate_dampened_pass(self):
        reports = ["75 79 76 79 80 81",
                   "75 72 76 77 78 81",
                   "75 74 73 72 71 81"]
        results = [self.solution.evaluate_new(report) for report in reports]
        self.assertEqual(results, [(0, 1), (0, 1), (0, 1)])
        
if __name__ == '__main__':
    unittest.main()