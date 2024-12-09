import unittest
from typing import List

from day_09 import Solution

SIMPLE_INPUT="291"
SIMPLE_INPUT_INITIAL_DISKMAP="00.........1"
SIMPLE_INPUT_FINAL_DISKMAP="001........."
SIMPLE_INPUT_CHECKSUM=2

AOC_INPUT="2333133121414131402"
AOC_INPUT_INITIAL_DISKMAP="00...111...2...333.44.5555.6666.777.888899"
AOC_INPUT_FINAL_DISKMAP="0099811188827773336446555566.............."
AOC_INPUT_CHECKSUM=1928

AOC_INPUT_UNFRAGMENTED_DISKMAP="00992111777.44.333....5555.6666.....8888.."
AOC_INPUT_UNFRAGMENTED_CHECKSUM=2858

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_load_disk_map_simple_input(self):
        self.solution.load_disk_map(SIMPLE_INPUT)
        self.assertEqual(self.solution.disk_map_to_string(), SIMPLE_INPUT_INITIAL_DISKMAP)

    def test_optimize_disk_map_simple_input(self):
        self.solution.load_disk_map(SIMPLE_INPUT)
        self.solution.optimize_disk_map()
        self.assertEqual(self.solution.optimized_disk_map_to_string(), SIMPLE_INPUT_FINAL_DISKMAP)

    def test_calculate_checksum_simple_input(self):
        self.solution.load_disk_map(SIMPLE_INPUT)
        self.solution.optimize_disk_map()
        self.assertEqual(self.solution.calculate_checksum(), SIMPLE_INPUT_CHECKSUM)

    def test_load_disk_map(self):
        self.solution.load_disk_map(AOC_INPUT)
        self.assertEqual(self.solution.disk_map_to_string(), AOC_INPUT_INITIAL_DISKMAP)

    def test_optimize_disk_map(self):
        self.solution.load_disk_map(AOC_INPUT)
        self.solution.optimize_disk_map()
        self.assertEqual(self.solution.optimized_disk_map_to_string(), AOC_INPUT_FINAL_DISKMAP)

    def test_calculate_checksum(self):
        self.solution.load_disk_map(AOC_INPUT)
        self.solution.optimize_disk_map()
        self.assertEqual(self.solution.calculate_checksum(), AOC_INPUT_CHECKSUM)

    def test_unfragmented_disk_map(self):
        self.solution.load_disk_map(AOC_INPUT)
        self.solution.unfragment_disk_map()
        self.assertEqual(self.solution.unfragmented_disk_map_to_string(), AOC_INPUT_UNFRAGMENTED_DISKMAP)

    def test_unfragmented_disk_map_checksum(self):
        self.solution.load_disk_map(AOC_INPUT)
        self.solution.unfragment_disk_map()
        self.assertEqual(self.solution.calculate_unfragmented_checksum(), AOC_INPUT_UNFRAGMENTED_CHECKSUM)

if __name__ == '__main__':
    unittest.main()