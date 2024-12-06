import unittest
from day_06 import Solution

AOC_INPUT = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

AOC_VISIT_MAP = """....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X.."""

AOC_OBSTACLE_LOCATIONS = [(3,6), (6,7), (7,7), (1,8), (3,8), (7,9)]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_load_map_aoc_input(self):
        self.solution.load_map(AOC_INPUT.splitlines())
        self.assertEqual(self.solution.map_width, 10)
        self.assertEqual(self.solution.map_height, 10)

    def test_create_visit_map_aoc_input(self):
        self.solution.load_map(AOC_INPUT.splitlines())
        self.solution.create_visit_map()
        # print()
        # [print([y for y in x]) for x in self.solution.visit_map]
        # print()
        # [print([y for y in x.strip()]) for x in AOC_VISIT_MAP.splitlines()]
        self.assertEqual(self.solution.visit_map, [[y for y in x.strip()] for x in AOC_VISIT_MAP.splitlines()])

    def test_count_distinct_positions_aoc_input(self):
        self.solution.load_map(AOC_INPUT.splitlines())
        self.solution.create_visit_map()
        self.assertEqual(self.solution.count_distinct_positions(), 41)

    def test_place_obstacles_aoc_input(self):
        self.solution.load_map(AOC_INPUT.splitlines())
        obstacles = self.solution.place_obstacles()
        self.assertEqual(len(obstacles), 6)
        self.assertCountEqual(obstacles, AOC_OBSTACLE_LOCATIONS)

if __name__ == '__main__':
    unittest.main()