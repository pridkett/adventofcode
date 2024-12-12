import unittest
from typing import List

from day_12 import Solution

AOC_INPUT_1="""AAAA
BBCD
BBCC
EEEC"""
AOC_OUTPUT_1=140
AOC_OUTPUT_1B=80

AOC_INPUT_2="""OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""
AOC_OUTPUT_2=772

AOC_INPUT_3="""RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
AOC_OUTPUT_3=1930
AOC_OUTPUT_3B=1206

AOC_INPUT_4="""EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""
AOC_OUTPUT_4B=236

AOC_INPUT_5="""AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""
AOC_OUTPUT_5B=368

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_aoc_input_1(self):
        self.solution.load(AOC_INPUT_1)
        self.assertEqual(self.solution.find_groups(), AOC_OUTPUT_1)

    def test_aoc_input_2(self):
        self.solution.load(AOC_INPUT_2)
        self.assertEqual(self.solution.find_groups(), AOC_OUTPUT_2)

    def test_aoc_input_3(self):
        self.solution.load(AOC_INPUT_3)
        self.assertEqual(self.solution.find_groups(), AOC_OUTPUT_3)

    def test_aoc_input_1b(self):
        self.solution.load(AOC_INPUT_1)
        self.assertEqual(self.solution.find_groups_2(), AOC_OUTPUT_1B)

    def test_aoc_input_4b(self):
        self.solution.load(AOC_INPUT_4)
        self.assertEqual(self.solution.find_groups_2(), AOC_OUTPUT_4B)

    def test_aoc_input_3b(self):
        self.solution.load(AOC_INPUT_3)
        self.assertEqual(self.solution.find_groups_2(), AOC_OUTPUT_3B)

    def test_aoc_input_5b(self):
        self.solution.load(AOC_INPUT_5)
        self.assertEqual(self.solution.find_groups_2(), AOC_OUTPUT_5B)

if __name__ == '__main__':
    unittest.main()