import unittest
from typing import List

from day_11 import Solution
SIMPLE_INPUT_1 = """0 1 10 99 999"""
SIMPLE_INPUT_1_OUTPUT = "1 2024 1 0 9 9 2021976"

AOC_INPUT="""125 17"""
AOC_INPUT_OUTPUT_1="""253000 1 7"""
AOC_INPUT_OUTPUT_2="""253 0 2024 14168"""
AOC_INPUT_OUTPUT_3="""512072 1 20 24 28676032"""
AOC_INPUT_OUTPUT_4="""512 72 2024 2 0 2 4 2867 6032"""
AOC_INPUT_OUTPUT_5="""1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32"""
AOC_INPUT_OUTPUT_6="""2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2"""
AOC_INPUT_25_BLINK_STONES=55312

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_simple_input_1(self):
        self.solution.load(SIMPLE_INPUT_1)
        self.solution.blink(1)
        self.assertEqual(self.solution.to_string(), SIMPLE_INPUT_1_OUTPUT)

    def test_aoc_input(self):
        self.solution.load(AOC_INPUT)
        self.solution.blink(1)
        self.assertEqual(self.solution.to_string(), AOC_INPUT_OUTPUT_1)
        self.solution.blink(1)
        self.assertEqual(self.solution.to_string(), AOC_INPUT_OUTPUT_2)
        self.solution.blink(1)
        self.assertEqual(self.solution.to_string(), AOC_INPUT_OUTPUT_3)
        self.solution.blink(1)
        self.assertEqual(self.solution.to_string(), AOC_INPUT_OUTPUT_4)
        self.solution.blink(1)
        self.assertEqual(self.solution.to_string(), AOC_INPUT_OUTPUT_5)
        self.solution.blink(1)
        self.assertEqual(self.solution.to_string(), AOC_INPUT_OUTPUT_6)
        self.assertEqual(self.solution.num_stones(), len(AOC_INPUT_OUTPUT_6.split()))
        self.solution.blink(19)
        self.assertEqual(self.solution.num_stones(), AOC_INPUT_25_BLINK_STONES)

    def test_multi_blink_simple_input(self):
        self.solution.load(SIMPLE_INPUT_1)
        stones = self.solution.multi_blink(1)
        self.assertEqual(stones, len(SIMPLE_INPUT_1_OUTPUT.split()))

    def test_multi_blink_aoc_input(self):
        self.solution.load(AOC_INPUT)
        stones = self.solution.multi_blink(1)
        self.assertEqual(stones, len(AOC_INPUT_OUTPUT_1.split()))
        stones = self.solution.multi_blink(2)
        self.assertEqual(stones, len(AOC_INPUT_OUTPUT_2.split()))
        stones = self.solution.multi_blink(3)
        self.assertEqual(stones, len(AOC_INPUT_OUTPUT_3.split()))
        stones = self.solution.multi_blink(4)
        self.assertEqual(stones, len(AOC_INPUT_OUTPUT_4.split()))
        stones = self.solution.multi_blink(5)
        self.assertEqual(stones, len(AOC_INPUT_OUTPUT_5.split()))
        stones = self.solution.multi_blink(6)
        self.assertEqual(stones, len(AOC_INPUT_OUTPUT_6.split()))

        self.solution.load(AOC_INPUT)
        stones = self.solution.multi_blink(25)
        self.assertEqual(stones, AOC_INPUT_25_BLINK_STONES)

    def test_multi_blink2_aoc_input(self):
        self.solution.load(AOC_INPUT)
        stones = self.solution.multi_blink2(1)
        self.assertEqual(stones, len(AOC_INPUT_OUTPUT_1.split()))
        stones = self.solution.multi_blink2(2)
        self.assertEqual(stones, len(AOC_INPUT_OUTPUT_2.split()))
        stones = self.solution.multi_blink2(3)
        self.assertEqual(stones, len(AOC_INPUT_OUTPUT_3.split()))
        stones = self.solution.multi_blink2(4)
        self.assertEqual(stones, len(AOC_INPUT_OUTPUT_4.split()))
        stones = self.solution.multi_blink2(5)
        self.assertEqual(stones, len(AOC_INPUT_OUTPUT_5.split()))
        stones = self.solution.multi_blink2(6)
        self.assertEqual(stones, len(AOC_INPUT_OUTPUT_6.split()))

        self.solution.load(AOC_INPUT)
        stones = self.solution.multi_blink2(25)
        self.assertEqual(stones, AOC_INPUT_25_BLINK_STONES)

if __name__ == '__main__':
    unittest.main()