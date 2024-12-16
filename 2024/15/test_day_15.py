import unittest

from day_15 import Solution

AOC_INPUT_1_MAP="""##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########"""
AOC_INPUT_1_INSTRUCTIONS="""<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
AOC_INPUT_1_FINAL_MAP="""##########
#.O.O.OOO#
#........#
#OO......#
#OO@.....#
#O#.....O#
#O.....OO#
#O.....OO#
#OO....OO#
##########"""
AOC_INPUT_1_GPS_SCORE=10092
AOC_INPUT_1_ADVANCED_MAP="""####################
##....[]....[]..[]##
##............[]..##
##..[][]....[]..[]##
##....[]@.....[]..##
##[]##....[]......##
##[]....[]....[]..##
##..[][]..[]..[][]##
##........[]......##
####################"""
AOC_INPUT_1_ADVANCED_FINAL_MAP="""####################
##[].......[].[][]##
##[]...........[].##
##[]........[][][]##
##[]......[]....[]##
##..##......[]....##
##..[]............##
##..@......[].[][]##
##......[][]..[]..##
####################"""
AOC_INPUT_1_ADVANCED_GPS_SCORE=9021

AOC_INPUT_2_MAP="""########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########"""
AOC_INPUT_2_INSTRUCTIONS="""<^^>>>vv<v>>v<<"""
AOC_INPUT_2_MAPS=["""########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########""",
"""########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########""",
"""########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########""",
"""########
#..@OO.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########""",
"""########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########""",
"""########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########""",
"""########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########""",
"""########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########""",
"""########
#....OO#
##.@...#
#...O..#
#.#.O..#
#...O..#
#...O..#
########""",
"""########
#....OO#
##.....#
#..@O..#
#.#.O..#
#...O..#
#...O..#
########""",
"""########
#....OO#
##.....#
#...@O.#
#.#.O..#
#...O..#
#...O..#
########""",
"""########
#....OO#
##.....#
#....@O#
#.#.O..#
#...O..#
#...O..#
########""",
"""########
#....OO#
##.....#
#.....O#
#.#.O@.#
#...O..#
#...O..#
########""",
"""########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########""",
"""########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########"""]
AOC_INPUT_2_GPS_SCORE=2028

AOC_INPUT_3_MAP="""#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######"""
AOC_INPUT_3_ADVANCED_MAP="""##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############"""
AOC_INPUT_3_INSTRUCTIONS="""<vv<<^^<<^^"""
AOC_INPUT_3_MAPS=["""##############
##......##..##
##..........##
##...[][]@..##
##....[]....##
##..........##
##############""",
"""##############
##......##..##
##..........##
##...[][]...##
##....[].@..##
##..........##
##############""",
"""##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.......@..##
##############""",
"""##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##......@...##
##############""",
"""##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.....@....##
##############""",
"""##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############""",
"""##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############""",
"""##############
##......##..##
##...[][]...##
##....[]....##
##....@.....##
##..........##
##############""",
"""##############
##......##..##
##...[][]...##
##....[]....##
##...@......##
##..........##
##############""",
"""##############
##......##..##
##...[][]...##
##...@[]....##
##..........##
##..........##
##############""",
"""##############
##...[].##..##
##...@.[]...##
##....[]....##
##..........##
##..........##
##############"""]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_aoc_input_1_load_map(self):
        self.solution.map = AOC_INPUT_1_MAP
        self.assertEqual(AOC_INPUT_1_MAP, self.solution.map)

    def test_aoc_input_1_run(self):
        self.solution.map = AOC_INPUT_1_MAP
        self.assertEqual(AOC_INPUT_1_MAP, self.solution.map)
        self.solution.instructions = AOC_INPUT_1_INSTRUCTIONS
        self.solution.run()
        self.assertEqual(AOC_INPUT_1_FINAL_MAP, self.solution.map)

    def test_aoc_input_1_gps_score(self):
        self.solution.map = AOC_INPUT_1_MAP
        self.solution.instructions = AOC_INPUT_1_INSTRUCTIONS
        self.solution.run()
        self.assertEqual(AOC_INPUT_1_GPS_SCORE, self.solution.get_gps_score())

    def test_aoc_input_2_load_map(self):
        self.solution.map = AOC_INPUT_2_MAP
        self.assertEqual(AOC_INPUT_2_MAP, self.solution.map)

    def test_aoc_input_2_maps(self):
        self.solution.map = AOC_INPUT_2_MAP
        self.solution.instructions = AOC_INPUT_2_INSTRUCTIONS
        for _, m in enumerate(AOC_INPUT_2_MAPS):
            self.solution.tick(1)
            self.assertEqual(m, self.solution.map)

    def test_aoc_input_2_gps_score(self):
        self.solution.map = AOC_INPUT_2_MAP
        self.solution.instructions = AOC_INPUT_2_INSTRUCTIONS
        self.solution.run()
        self.assertEqual(AOC_INPUT_2_GPS_SCORE, self.solution.get_gps_score())

    def test_aoc_input_2_full_parse(self):
        self.solution.load("\n".join([AOC_INPUT_2_MAP, "", AOC_INPUT_2_INSTRUCTIONS]))
        self.solution.run()
        self.assertEqual(AOC_INPUT_2_GPS_SCORE, self.solution.get_gps_score())

    def test_aoc_input_1_advanced_map(self):
        self.solution.set_advanced_map(AOC_INPUT_1_MAP)
        self.solution.instructions = AOC_INPUT_1_INSTRUCTIONS
        self.assertEqual(AOC_INPUT_1_ADVANCED_MAP, self.solution.map)
        self.solution.run()
        self.assertEqual(AOC_INPUT_1_ADVANCED_FINAL_MAP, self.solution.map)

    def test_aoc_input_1_advanced_gps(self):
        self.solution.set_advanced_map(AOC_INPUT_1_MAP)
        self.solution.instructions = AOC_INPUT_1_INSTRUCTIONS
        self.assertEqual(AOC_INPUT_1_ADVANCED_MAP, self.solution.map)
        self.solution.run()
        self.assertEqual(AOC_INPUT_1_ADVANCED_FINAL_MAP, self.solution.map)
        self.assertEqual(AOC_INPUT_1_ADVANCED_GPS_SCORE, self.solution.get_gps_score())

    def test_aoc_input_3_maps(self):
        self.solution.set_advanced_map(AOC_INPUT_3_MAP)
        self.solution.instructions = AOC_INPUT_3_INSTRUCTIONS
        self.assertEqual(AOC_INPUT_3_ADVANCED_MAP, self.solution.map)
        for _, m in enumerate(AOC_INPUT_3_MAPS):
            self.solution.tick(1)
            self.assertEqual(m, self.solution.map)

if __name__ == '__main__':
    unittest.main()