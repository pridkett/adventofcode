import unittest
from day_03 import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_parse_line_single_multiplication(self):
        line = "mul(2,3)"
        result = self.solution.parse_line(line)
        self.assertEqual(result, 6)

    def test_parse_line_multiple_multiplications(self):
        line = "mul(2,3) mul(4,5)"
        result = self.solution.parse_line(line)
        self.assertEqual(result, 26)

    def test_parse_line_no_multiplication(self):
        line = "add(2,3)"
        result = self.solution.parse_line(line)
        self.assertEqual(result, 0)

    def test_parse_line_advanced_with_do(self):
        line = "do() mul(2,3)"
        result = self.solution.parse_line_advanced(line)
        self.assertEqual(result, 6)

    def test_parse_line_advanced_with_dont(self):
        line = "don't() mul(2,3)"
        result = self.solution.parse_line_advanced(line)
        self.assertEqual(result, 0)

    def test_parse_line_advanced_mixed_instructions(self):
        line = "do() mul(2,3) don't() mul(4,5) do() mul(1,1)"
        result = self.solution.parse_line_advanced(line)
        self.assertEqual(result, 7)

    def test_parse_line_advanced_no_instructions(self):
        line = "mul(3,3)"
        result = self.solution.parse_line_advanced(line)
        self.assertEqual(result, 9)

if __name__ == '__main__':
    unittest.main()