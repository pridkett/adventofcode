import unittest

from day_16 import Solution

AOC_INPUT_1_MAP="""###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""
AOC_INPUT_1_MINIMUM_SCORE=7036
AOC_INPUT_1_PATH_LENGTH=45

AOC_INPUT_2_MAP="""#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""
AOC_INPUT_2_MINIMUM_SCORE=11048
AOC_INPUT_2_PATH_LENGTH=64

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_aoc_input_1_load_map(self):
        self.solution.map = AOC_INPUT_1_MAP
        self.assertEqual(AOC_INPUT_1_MAP, self.solution.map)

    def test_aoc_input_1_run(self):
        self.solution.map = AOC_INPUT_1_MAP
        self.assertEqual(AOC_INPUT_1_MAP, self.solution.map)
        score, _ = self.solution.run()
        self.assertEqual(score, AOC_INPUT_1_MINIMUM_SCORE)

    def test_aoc_input_1_path_length(self):
        self.solution.map = AOC_INPUT_1_MAP
        self.assertEqual(AOC_INPUT_1_MAP, self.solution.map)
        score, path_length = self.solution.run()
        self.assertEqual(score, AOC_INPUT_1_MINIMUM_SCORE)
        self.assertEqual(path_length, AOC_INPUT_1_PATH_LENGTH)

    def test_aoc_input_2_load_map(self):
        self.solution.map = AOC_INPUT_2_MAP
        self.assertEqual(AOC_INPUT_2_MAP, self.solution.map)

    def test_aoc_input_2_run(self):
        self.solution.map = AOC_INPUT_2_MAP
        self.assertEqual(AOC_INPUT_2_MAP, self.solution.map)
        score, _ = self.solution.run()
        self.assertEqual(score, AOC_INPUT_2_MINIMUM_SCORE)

    def test_aoc_input_2_path_length(self):
        self.solution.map = AOC_INPUT_2_MAP
        self.assertEqual(AOC_INPUT_2_MAP, self.solution.map)
        score, path_length = self.solution.run()
        self.assertEqual(score, AOC_INPUT_2_MINIMUM_SCORE)
        self.assertEqual(path_length, AOC_INPUT_2_PATH_LENGTH)

if __name__ == '__main__':
    unittest.main()