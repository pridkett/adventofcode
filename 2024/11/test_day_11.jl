using Test
include("./day_11.jl")

SIMPLE_INPUT_1 = """0 1 10 99 999"""
SIMPLE_INPUT_1_OUTPUT = "1 2024 1 0 9 9 2021976"

AOC_INPUT="""125 17"""
AOC_INPUT_OUTPUT_1="""253000 1 7"""
AOC_INPUT_OUTPUT_2="""253 0 2024 14168"""
AOC_INPUT_OUTPUT_3="""512072 1 20 24 28676032"""
AOC_INPUT_OUTPUT_4="""512 72 2024 2 0 2 4 2867 6032"""
AOC_INPUT_OUTPUT_5="""1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32"""
AOC_INPUT_OUTPUT_6="""2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2"""
AOC_INPUT_25_BLINK_STONES=55312

function test_solution()

    @testset "Simple Input" begin
        s = Solution(SIMPLE_INPUT_1)
        @test multi_blink(s, 1)==length(split(SIMPLE_INPUT_1_OUTPUT))
    end

    @testset "AOC Input Part 1" begin
        s = Solution(AOC_INPUT)
        @test multi_blink(s, 6) == length(split(AOC_INPUT_OUTPUT_6))
        @test multi_blink(s, 25) == AOC_INPUT_25_BLINK_STONES
    end
end

test_solution()
