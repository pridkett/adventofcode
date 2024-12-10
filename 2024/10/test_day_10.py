import unittest
from typing import List

from day_10 import Solution
AOC_SIMPLE_INPUT_1 = """...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9"""
AOC_SIMPLE_INPUT_1_TRAILHEAD_VALUES = [2]
AOC_SIMPLE_INPUT_1_TRAILHEAD_SUM = 2

AOC_SIMPLE_INPUT_2 = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""
AOC_SIMPLE_INPUT_2_TRAILHEAD_VALUES = [4]
AOC_SIMPLE_INPUT_2_TRAILHEAD_SUM = 4

AOC_SIMPLE_INPUT_3 = """10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01"""
AOC_SIMPLE_INPUT_3_TRAILHEAD_VALUES = [1,2]
AOC_SIMPLE_INPUT_3_TRAILHEAD_SUM = 3

AOC_INPUT="""89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
AOC_INPUT_TRAILHEAD_VALUES = [5, 6, 5, 3, 1, 3, 5, 3, 5]
AOC_INPUT_TRAILHEAD_SUM = 36

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_load_disk_map_simple_input_1(self):
        self.solution.load_trailmap([x.strip() for x in AOC_SIMPLE_INPUT_1.splitlines()])
        self.assertEqual(self.solution.trailmap_to_string(), AOC_SIMPLE_INPUT_1)

    def test_find_trails_simple_input_1(self):
        self.solution.load_trailmap([x.strip() for x in AOC_SIMPLE_INPUT_1.splitlines()])
        self.assertEqual([len(x) for x in self.solution.find_trails()], AOC_SIMPLE_INPUT_1_TRAILHEAD_VALUES)

    def test_find_trailhead_sum_simple_input_1(self):
        self.solution.load_trailmap([x.strip() for x in AOC_SIMPLE_INPUT_1.splitlines()])
        self.assertEqual(sum([len(x) for x in self.solution.find_trails()]), AOC_SIMPLE_INPUT_1_TRAILHEAD_SUM)

    def test_load_disk_map_simple_input_2(self):
        self.solution.load_trailmap([x.strip() for x in AOC_SIMPLE_INPUT_2.splitlines()])
        self.assertEqual(self.solution.trailmap_to_string(), AOC_SIMPLE_INPUT_2)

    def test_find_trails_simple_input_2(self):
        self.solution.load_trailmap([x.strip() for x in AOC_SIMPLE_INPUT_2.splitlines()])
        self.assertEqual([len(x) for x in self.solution.find_trails()], AOC_SIMPLE_INPUT_2_TRAILHEAD_VALUES)

    def test_find_trailhead_sum_simple_input_2(self):
        self.solution.load_trailmap([x.strip() for x in AOC_SIMPLE_INPUT_2.splitlines()])
        self.assertEqual(sum([len(x) for x in self.solution.find_trails()]), AOC_SIMPLE_INPUT_2_TRAILHEAD_SUM)

    def test_load_disk_map_simple_input_3(self):
        self.solution.load_trailmap([x.strip() for x in AOC_SIMPLE_INPUT_3.splitlines()])
        self.assertEqual(self.solution.trailmap_to_string(), AOC_SIMPLE_INPUT_3)

    def test_find_trails_simple_input_3(self):
        self.solution.load_trailmap([x.strip() for x in AOC_SIMPLE_INPUT_3.splitlines()])
        self.assertEqual([len(x) for x in self.solution.find_trails()], AOC_SIMPLE_INPUT_3_TRAILHEAD_VALUES)

    def test_find_trailhead_sum_simple_input_3(self):
        self.solution.load_trailmap([x.strip() for x in AOC_SIMPLE_INPUT_3.splitlines()])
        self.assertEqual(sum([len(x) for x in self.solution.find_trails()]), AOC_SIMPLE_INPUT_3_TRAILHEAD_SUM)

    def test_load_disk_map_aoc_input(self):
        self.solution.load_trailmap([x.strip() for x in AOC_INPUT.splitlines()])
        self.assertEqual(self.solution.trailmap_to_string(), AOC_INPUT)

    def test_find_trails_aoc_input(self):
        self.solution.load_trailmap([x.strip() for x in AOC_INPUT.splitlines()])
        self.assertEqual([len(x) for x in self.solution.find_trails()], AOC_INPUT_TRAILHEAD_VALUES)

    def test_find_trailhead_aoc_input(self):
        self.solution.load_trailmap([x.strip() for x in AOC_INPUT.splitlines()])
        self.assertEqual(sum([len(x) for x in self.solution.find_trails()]), AOC_INPUT_TRAILHEAD_SUM)
    



    # def test_optimize_disk_map_simple_input(self):
    #     self.solution.load_disk_map(SIMPLE_INPUT)
    #     self.solution.optimize_disk_map()
    #     self.assertEqual(self.solution.optimized_disk_map_to_string(), SIMPLE_INPUT_FINAL_DISKMAP)

    # def test_calculate_checksum_simple_input(self):
    #     self.solution.load_disk_map(SIMPLE_INPUT)
    #     self.solution.optimize_disk_map()
    #     self.assertEqual(self.solution.calculate_checksum(), SIMPLE_INPUT_CHECKSUM)

    # def test_load_disk_map(self):
    #     self.solution.load_disk_map(AOC_INPUT)
    #     self.assertEqual(self.solution.disk_map_to_string(), AOC_INPUT_INITIAL_DISKMAP)

    # def test_optimize_disk_map(self):
    #     self.solution.load_disk_map(AOC_INPUT)
    #     self.solution.optimize_disk_map()
    #     self.assertEqual(self.solution.optimized_disk_map_to_string(), AOC_INPUT_FINAL_DISKMAP)

    # def test_calculate_checksum(self):
    #     self.solution.load_disk_map(AOC_INPUT)
    #     self.solution.optimize_disk_map()
    #     self.assertEqual(self.solution.calculate_checksum(), AOC_INPUT_CHECKSUM)

    # def test_unfragmented_disk_map(self):
    #     self.solution.load_disk_map(AOC_INPUT)
    #     self.solution.unfragment_disk_map()
    #     self.assertEqual(self.solution.unfragmented_disk_map_to_string(), AOC_INPUT_UNFRAGMENTED_DISKMAP)

    # def test_unfragmented_disk_map_checksum(self):
    #     self.solution.load_disk_map(AOC_INPUT)
    #     self.solution.unfragment_disk_map()
    #     self.assertEqual(self.solution.calculate_unfragmented_checksum(), AOC_INPUT_UNFRAGMENTED_CHECKSUM)

if __name__ == '__main__':
    unittest.main()