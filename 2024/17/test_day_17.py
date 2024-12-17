import unittest

from day_17 import Solution

AOC_INPUT_1="""Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""
AOC_INPUT_1_OUTPUT="""4,6,3,5,6,3,5,2,1,0"""

AOC_INPUT_2="""Register A: 729
Register B: 0
Register C: 9

Program: 2,6"""
AOC_INPUT_2_REGISTER_OUTPUT={'B': 1}

AOC_INPUT_3="""Register A: 10
Register B: 0
Register C: 0

Program: 5,0,5,1,5,4"""
AOC_INPUT_3_OUTPUT="""0,1,2"""

AOC_INPUT_4="""Register A: 2024
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""
AOC_INPUT_4_OUTPUT="""4,2,5,6,7,7,7,7,3,1,0"""
AOC_INPUT_4_REGISTER_OUTPUT={'A': 0}

AOC_INPUT_5="""Register A: 0
Register B: 29
Register C: 0

Program: 1,7"""
AOC_INPUT_5_REGISTER_OUTPUT={'B': 26}

AOC_INPUT_6="""Register A: 0
Register B: 2024
Register C: 43690

Program: 4,0"""
AOC_INPUT_6_REGISTER_OUTPUT={'B': 44354}

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_aoc_input_1_load(self):
        self.solution.load(AOC_INPUT_1)
        output = self.solution.run()
        self.assertEqual(AOC_INPUT_1_OUTPUT, output)

    def test_aoc_input_2(self):
        self.solution.load(AOC_INPUT_2)
        self.solution.run()
        for k in AOC_INPUT_2_REGISTER_OUTPUT:
            self.assertEqual(AOC_INPUT_2_REGISTER_OUTPUT[k], self.solution.registers[k])

    def test_aoc_input_3(self):
        self.solution.load(AOC_INPUT_3)
        output = self.solution.run()
        self.assertEqual(AOC_INPUT_3_OUTPUT, output)

    def test_aoc_input_4(self):
        self.solution.load(AOC_INPUT_4)
        output = self.solution.run()
        self.assertEqual(AOC_INPUT_4_OUTPUT, output)
        for k,v in AOC_INPUT_4_REGISTER_OUTPUT.items():
            self.assertEqual(v, self.solution.registers[k])

    def test_aoc_input_5(self):
        self.solution.load(AOC_INPUT_5)
        self.solution.run()
        for k,v in AOC_INPUT_5_REGISTER_OUTPUT.items():
            self.assertEqual(v, self.solution.registers[k])

    def test_aoc_input_6(self):
        self.solution.load(AOC_INPUT_6)
        self.solution.run()
        for k,v in AOC_INPUT_6_REGISTER_OUTPUT.items():
            self.assertEqual(v, self.solution.registers[k])

if __name__ == '__main__':
    unittest.main()