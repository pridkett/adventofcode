import unittest
from typing import List

from day_08 import Solution

AOC_SIMPLE_INPUT_1 = """..........
...#......
..........
....a.....
..........
.....a....
..........
......#...
..........
.........."""
AOC_SIMPLE_INPUT_1_ANTENNA_LOCATIONS = {'a': [(3, 4), (5, 5)]}
AOC_SIMPLE_INPUT_1_ANTINODE_LOCATIONS = [(1,3), (7,6)]

AOC_SIMPLE_INPUT_2 = """..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......#...
..........
.........."""
AOC_SIMPLE_INPUT_2_ANTENNA_LOCATIONS = {'a': [(3, 4), (5, 5), (4, 8)]}
AOC_SIMPLE_INPUT_2_ANTINODE_LOCATIONS = [(1,3), (7,6), (2,0), (6,2)]

AOC_INPUT = """......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#."""
AOC_INPUT_ANTENNA_LOCATIONS = {'0':[(1,8), (2,5), (3,7), (4,4)],'A': [(5, 6), (8, 8), (9, 9)]}
AOC_INPUT_ANTINODE_LOCATIONS = [(0,6), (0,11), (1,3), (2,4), (2,10), (3,2), (4,9), (5,1), (5,6), (6,3), (7,0), (7,7), (10,10), (11,10)]

AOC_SIMPLE_RESONANT_INPUT = """T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
.........."""
AOC_SIMPLE_RESONANT_INPUT_ANTENNA_LOCATIONS = {'T': [(0, 0),  (1, 3), (2, 1)]}
AOC_SIMPLE_RESONANT_INPUT_ANTINODE_LOCATIONS = [(0, 0), (0, 5), (1, 3), (2, 1), (2,6),
                                                     (3,9), (4,2), (6,3), (8,4)]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_load_map_simple(self):
        self.solution.load_map(AOC_SIMPLE_INPUT_1)
        self.assertEqual(self.solution.antennas.keys(), AOC_SIMPLE_INPUT_1_ANTENNA_LOCATIONS.keys())
        for key in AOC_SIMPLE_INPUT_1_ANTENNA_LOCATIONS.keys():
            self.assertCountEqual(self.solution.antennas[key], AOC_SIMPLE_INPUT_1_ANTENNA_LOCATIONS[key])

    def test_find_antinodes_simple_1(self):
        self.solution.load_map(AOC_SIMPLE_INPUT_1)
        self.assertCountEqual(self.solution.antennas.keys(), AOC_SIMPLE_INPUT_1_ANTENNA_LOCATIONS.keys())
        for key in AOC_SIMPLE_INPUT_1_ANTENNA_LOCATIONS.keys():
            self.assertCountEqual(self.solution.antennas[key], AOC_SIMPLE_INPUT_1_ANTENNA_LOCATIONS[key])
        self.assertEqual(len(self.solution.antinodes), len(AOC_SIMPLE_INPUT_1_ANTINODE_LOCATIONS))
        self.assertCountEqual(self.solution.antinodes, list(AOC_SIMPLE_INPUT_1_ANTINODE_LOCATIONS))

    def test_find_antinodes_simple_2(self):
        self.solution.load_map(AOC_SIMPLE_INPUT_2)
        self.assertCountEqual(self.solution.antennas.keys(), AOC_SIMPLE_INPUT_2_ANTENNA_LOCATIONS.keys())
        for key in AOC_SIMPLE_INPUT_2_ANTENNA_LOCATIONS.keys():
            self.assertCountEqual(self.solution.antennas[key], AOC_SIMPLE_INPUT_2_ANTENNA_LOCATIONS[key])
        self.assertEqual(len(self.solution.antinodes), len(AOC_SIMPLE_INPUT_2_ANTINODE_LOCATIONS))
        self.assertCountEqual(self.solution.antinodes, AOC_SIMPLE_INPUT_2_ANTINODE_LOCATIONS)

    def test_find_antinodes_aoc_input(self):
        self.solution.load_map(AOC_INPUT)
        self.assertCountEqual(self.solution.antennas.keys(), AOC_INPUT_ANTENNA_LOCATIONS.keys())
        for key in AOC_INPUT_ANTENNA_LOCATIONS.keys():
            self.assertCountEqual(self.solution.antennas[key], AOC_INPUT_ANTENNA_LOCATIONS[key])
        self.assertEqual(len(self.solution.antinodes), len(AOC_INPUT_ANTINODE_LOCATIONS))
        self.assertCountEqual(self.solution.antinodes, AOC_INPUT_ANTINODE_LOCATIONS)

    def test_find_resonant_antinodes_simple_aoc_input(self):
        self.solution.load_map(AOC_SIMPLE_RESONANT_INPUT)
        self.assertCountEqual(self.solution.antennas.keys(), AOC_SIMPLE_RESONANT_INPUT_ANTENNA_LOCATIONS.keys())
        for key in AOC_SIMPLE_RESONANT_INPUT_ANTENNA_LOCATIONS.keys():
             self.assertCountEqual(self.solution.antennas[key], AOC_SIMPLE_RESONANT_INPUT_ANTENNA_LOCATIONS[key])
        self.assertEqual(len(self.solution.resonant_antinodes), len(AOC_SIMPLE_RESONANT_INPUT_ANTINODE_LOCATIONS))
        self.assertCountEqual(self.solution.resonant_antinodes, AOC_SIMPLE_RESONANT_INPUT_ANTINODE_LOCATIONS)

if __name__ == '__main__':
    unittest.main()