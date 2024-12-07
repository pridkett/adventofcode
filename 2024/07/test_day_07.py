import unittest
from typing import List

from day_07 import Solution

AOC_INPUT = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

AOC_OPERATORS: List[List[str]] = [['*'], ['+', '*'], [], [], [], [], [], [], ['+', '*', '+']]
AOC_TARGET = 3749

AOC_CONCATENATION_INPUT = """156: 15 6
7290: 6 8 6 15
192: 17 8 14"""
AOC_CONCATENATION_OPERATORS: List[List[str]] = [['||'], ['*', '||', '*'], ['||', '+']]
AOC_CONCATENATION_TARGET = 7638

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()


    def test_find_operators_simple(self):
        test_input = """120: 10 12
        4392: 48 13 72"""

        operators = self.solution.find_operators(test_input)
        self.assertEqual([x.operators for x in operators], [['*'], ['+', '*']])

    def test_find_operators_simple_sum(self):
        test_input = """120: 10 12
        4392: 48 13 72"""

        operators = self.solution.find_operators(test_input)
        self.assertEqual(sum([x.target for x in operators if x.operators != []]), 4512)

    def test_find_operators_aoc_input(self):
        operators = self.solution.find_operators(AOC_INPUT)
        self.assertEqual([x.operators for x in operators], AOC_OPERATORS)

    def test_find_operators_aoc_input_sum(self):
        operators = self.solution.find_operators(AOC_INPUT)
        self.assertEqual(sum([x.target for x in operators if x.operators != []]), AOC_TARGET)

    def test_find_operators_concat_aoc_input(self):
        operators = self.solution.find_operators_concat(AOC_CONCATENATION_INPUT)
        self.assertEqual([x.operators for x in operators], AOC_CONCATENATION_OPERATORS)

    def test_find_operators_concat_aoc_input_sum(self):
        operators = self.solution.find_operators_concat(AOC_CONCATENATION_INPUT)
        self.assertEqual(sum([x.target for x in operators if x.operators != []]), AOC_CONCATENATION_TARGET)

if __name__ == '__main__':
    unittest.main()