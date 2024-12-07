using Test
include("./day_06.jl")

# Unit tests
AOC_INPUT="""....#.....
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

# these needed to be incremented 1 because Julia is 1-indexed
AOC_OBSTACLE_LOCATIONS = [(4,7), (7,8), (8,8), (2,9), (4,9), (8,10)]
function test_solution()
    
    solution = Solution()
    load_map(solution, [String(strip(x)) for x in split(AOC_INPUT, "\n")])
    @test solution.map_width == 10
    @test solution.map_height == 10

    create_visit_map(solution)

    @test solution.visit_map == [collect(String(strip(x))) for x in split(AOC_VISIT_MAP, "\n")]

    @test count_distinct_positions(solution) == 41

    solution = Solution()
    load_map(solution, [String(strip(x)) for x in split(AOC_INPUT, "\n")])
    obstacles = place_obstacles(solution)
    
    @test length(obstacles) == 6
    @test sort(obstacles) == sort(AOC_OBSTACLE_LOCATIONS)
end

test_solution()
