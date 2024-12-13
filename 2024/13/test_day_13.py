import unittest

from day_13 import Solution

AOC_INPUT_1="""Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400"""
AOC_INPUT_1_COST=280
AOC_INPUT_1_A_PRESSES=80
AOC_INPUT_1_B_PRESSES=40

AOC_INPUT_2="""Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176"""
AOC_INPUT_2_COST=-1

AOC_INPUT_3="""Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450"""
AOC_INPUT_3_COST=200
AOC_INPUT_3_A_PRESSES=38
AOC_INPUT_3_B_PRESSES=86

AOC_INPUT_4="""Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""
AOC_INPUT_4_COST=-1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_aoc_input_1(self):
        (cost, a_presses, b_presses) = self.solution.load(AOC_INPUT_1)

        self.assertEqual(cost, AOC_INPUT_1_COST)
        self.assertEqual(a_presses, AOC_INPUT_1_A_PRESSES)
        self.assertEqual(b_presses, AOC_INPUT_1_B_PRESSES)


    def test_aoc_input_2(self):
        (cost, a_presses, b_presses) = self.solution.load(AOC_INPUT_2)
        self.assertEqual(cost, AOC_INPUT_2_COST)
        
    def test_aoc_input_3(self):
        (cost, a_presses, b_presses) = self.solution.load(AOC_INPUT_3)
        self.assertEqual(cost, AOC_INPUT_3_COST)
        self.assertEqual(a_presses, AOC_INPUT_3_A_PRESSES)
        self.assertEqual(b_presses, AOC_INPUT_3_B_PRESSES)

    def test_aoc_input_4(self):
        (cost, a_presses, b_presses) = self.solution.load(AOC_INPUT_4)
        self.assertEqual(cost, AOC_INPUT_4_COST)
        
if __name__ == '__main__':
    unittest.main()