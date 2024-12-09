using Test
include("./day_08.jl")

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
AOC_SIMPLE_INPUT_1_ANTENNA_LOCATIONS = Dict('a' => [(4, 5), (6, 6)])
AOC_SIMPLE_INPUT_1_ANTINODE_LOCATIONS = Set([(2,4), (8,7)])

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
AOC_SIMPLE_INPUT_2_ANTENNA_LOCATIONS = Dict('a' => [(4, 5), (6, 6), (5, 9)])
AOC_SIMPLE_INPUT_2_ANTINODE_LOCATIONS = Set([(2,4), (8,7), (3,1), (7,3)])

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
AOC_INPUT_ANTENNA_LOCATIONS = Dict('0' => [(2,9), (3,6), (4,8), (5,5)],'A' => [(6, 7), (9, 9), (10, 10)])
AOC_INPUT_ANTINODE_LOCATIONS = Set([(1,7), (1,12), (2,4), (3,5), (3,11), (4,3), (5,10), (6,2), (6,7), (7,4), (8,1), (8,8), (11,11), (12,11)])

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
AOC_SIMPLE_RESONANT_INPUT_ANTENNA_LOCATIONS = Dict('T' => [(1, 1), (2, 4), (3, 2)])
AOC_SIMPLE_RESONANT_INPUT_ANTINODE_LOCATIONS = Set([(1, 1), (1, 6), (2, 4), (3, 2), (3,7),
                                                     (4,10), (5,3), (7,4), (9,5)])


function test_solution()

    @testset "Simple Input 1" begin
        solution = parse_input(AOC_SIMPLE_INPUT_1)
        @test solution.width == 10
        @test solution.height == 10
        antennas = find_antenna_locations(solution)
        @test keys(antennas)==keys(AOC_SIMPLE_INPUT_1_ANTENNA_LOCATIONS)
        for key in keys(AOC_SIMPLE_INPUT_1_ANTENNA_LOCATIONS)
            @test sort(antennas[key])==sort(AOC_SIMPLE_INPUT_1_ANTENNA_LOCATIONS[key])
        end
        @test find_antinode_locations(solution)==AOC_SIMPLE_INPUT_1_ANTINODE_LOCATIONS
    end

    @testset "Simple Input 2" begin
        solution = parse_input(AOC_SIMPLE_INPUT_2)
        antennas = find_antenna_locations(solution)
        @test keys(antennas)==keys(AOC_SIMPLE_INPUT_2_ANTENNA_LOCATIONS)
        for key in keys(AOC_SIMPLE_INPUT_2_ANTENNA_LOCATIONS)
            @test sort(antennas[key])==sort(AOC_SIMPLE_INPUT_2_ANTENNA_LOCATIONS[key])
        end
        @test find_antinode_locations(solution)==AOC_SIMPLE_INPUT_2_ANTINODE_LOCATIONS
    end

    @testset "AOC Part 1 Input" begin
        solution = parse_input(AOC_INPUT)
        antennas = find_antenna_locations(solution)
        @test keys(antennas)==keys(AOC_INPUT_ANTENNA_LOCATIONS)
        for key in keys(AOC_INPUT_ANTENNA_LOCATIONS)
            @test sort(antennas[key])==sort(AOC_INPUT_ANTENNA_LOCATIONS[key])
        end
        @test find_antinode_locations(solution)==AOC_INPUT_ANTINODE_LOCATIONS
    end

    @testset "Simple Resonant Input" begin
        solution = parse_input(AOC_SIMPLE_RESONANT_INPUT)
        @test find_antenna_locations(solution)==AOC_SIMPLE_RESONANT_INPUT_ANTENNA_LOCATIONS
        @test find_resonant_antinode_locations(solution)==AOC_SIMPLE_RESONANT_INPUT_ANTINODE_LOCATIONS
    end

    # @testset 
    # test_input = """120: 10 12
    #     4392: 48 13 72"""
    # operators = find_operators([String(strip(x)) for x in split(test_input, "\n")])
    # @test [x.operators for x in operators]==[['*'], ['+', '*']]
    # @test sum([x.target for x in operators if x.operators != []])==4512

    # operators = find_operators([String(strip(x)) for x in split(AOC_INPUT, "\n")])
    # @test [x.operators for x in operators]==AOC_OPERATORS
    # @test sum([x.target for x in operators if x.operators != []])==AOC_TARGET

    # operators = find_operators_concat([String(strip(x)) for x in split(AOC_CONCATENATION_INPUT, "\n")])
    # @test [x.operators for x in operators]==AOC_CONCATENATION_OPERATORS
    # @test sum([x.target for x in operators if x.operators != []])==AOC_CONCATENATION_TARGET
end

test_solution()
