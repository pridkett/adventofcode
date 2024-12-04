import unittest
from day_04 import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_find_words_aoc_input(self):
        words = [x.strip() for x in """....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX""".splitlines()]
        result = self.solution.find_words(words, "XMAS")
        self.assertEqual(result, 18)

    def test_find_words_simple_input(self):
        words = [x.strip() for x in """SSXMAS
                 SAMXMS""".splitlines()]
        result = self.solution.find_words(words, "XMAS")
        self.assertEqual(result, 2)

    def test_find_words_simple_diagonal(self):
        words = [x.strip() for x in """XZZS
                                       ZMAZ
                                       ZMAZ
                                       XZZS""".splitlines()]
        result = self.solution.find_words(words, "XMAS")
        self.assertEqual(result, 2)

    def test_find_words_x_simple_input(self):
        words = [x.strip() for x in """M.S
                                       .A.
                                       M.S""".splitlines()]
        result = self.solution.find_words_x(words, "MAS")
        self.assertEqual(result, 1)

    def test_find_words_x_reverse_input(self):
        words = [x.strip() for x in """S.M
                                       .A.
                                       S.M""".splitlines()]
        result = self.solution.find_words_x(words, "MAS")
        self.assertEqual(result, 1)

    def test_find_words_x_mixed_input(self):
        words = [x.strip() for x in """M.M
                                       .A.
                                       S.S""".splitlines()]
        result = self.solution.find_words_x(words, "MAS")
        self.assertEqual(result, 1)

    def test_find_words_x_superfluous_input(self):
        words = [x.strip() for x in """M.M
                                       .A.
                                       M.M""".splitlines()]
        result = self.solution.find_words_x(words, "MAS")
        self.assertEqual(result, 0)

    def test_find_words_x_aoc_input(self):
        words = [x.strip() for x in """.M.S......
                                       ..A..MSMS.
                                       .M.S.MAA..
                                       ..A.ASMSM.
                                       .M.S.M....
                                       ..........
                                       S.S.S.S.S.
                                       .A.A.A.A..
                                       M.M.M.M.M.
                                       ..........""".splitlines()]
        result = self.solution.find_words_x(words, "MAS")
        self.assertEqual(result, 9)
if __name__ == '__main__':
    unittest.main()