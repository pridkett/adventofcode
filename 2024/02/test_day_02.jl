using Test
include("./day_02.jl")

# Unit tests
function test_solution()
    solution = Solution()

    # AOC Provided Data
    @test evaluate(solution, "7 6 4 2 1") == (1, 1)
    @test evaluate(solution, "1 2 7 8 9") == (0, 0)
    @test evaluate(solution, "9 7 6 2 1") == (0, 0)
    @test evaluate(solution, "1 3 2 4 5") == (0, 1)
    @test evaluate(solution, "8 6 4 4 1") == (0, 1)
    @test evaluate(solution, "1 3 6 7 9") == (1, 1)

    # My Data

    # Dampened Fails
    @test evaluate(solution, "90 93 90 83 82 80 79") == (0, 0)
    @test evaluate(solution, "24 20 19 18 18 17 10") == (0, 0)
    @test evaluate(solution, "16 21 27 29 31 33 35 40") == (0, 0)
    
    # Dampened Pass
    @test evaluate(solution, "75 79 76 79 80 81") == (0, 1)
    @test evaluate(solution, "75 72 76 77 78 81") == (0, 1)
    @test evaluate(solution, "75 74 73 72 71 81") == (0, 1)
end

test_solution()



