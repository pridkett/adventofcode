using Test
include("./day_07.jl")

# Unit tests
AOC_INPUT = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

# note - for some of these tests the order of the operations may be
# different. So, they might fail just because.

AOC_OPERATORS::Vector{Vector{Char}} = [['*'], ['*', '+'], [], [], [], [], [], [], ['+', '*', '+']]
AOC_TARGET = 3749

AOC_CONCATENATION_INPUT = """156: 15 6
7290: 6 8 6 15
192: 17 8 14"""
AOC_CONCATENATION_OPERATORS::Vector{Vector{Char}} = [['|'], ['*', '|', '*'], ['|', '+']]
AOC_CONCATENATION_TARGET = 7638

function test_solution()
    test_input = """120: 10 12
        4392: 48 13 72"""
    operators = find_operators([String(strip(x)) for x in split(test_input, "\n")])
    @test [x.operators for x in operators]==[['*'], ['+', '*']]
    @test sum([x.target for x in operators if x.operators != []])==4512

    operators = find_operators([String(strip(x)) for x in split(AOC_INPUT, "\n")])
    @test [x.operators for x in operators]==AOC_OPERATORS
    @test sum([x.target for x in operators if x.operators != []])==AOC_TARGET

    operators = find_operators_concat([String(strip(x)) for x in split(AOC_CONCATENATION_INPUT, "\n")])
    @test [x.operators for x in operators]==AOC_CONCATENATION_OPERATORS
    @test sum([x.target for x in operators if x.operators != []])==AOC_CONCATENATION_TARGET
end

test_solution()
