using Test
include("./day_03.jl")

# Unit tests
function test_solution()
    solution = Solution()

    # Test parse_line
    @test parse_line(solution, "mul(2,3)") == 6
    @test parse_line(solution, "mul(2,3) mul(4,5)") == 26
    @test parse_line(solution, "add(2,3)") == 0

    # Test parse_line_advanced
    solution = Solution()
    @test parse_line_advanced(solution, "do() mul(2,3)") == 6

    solution = Solution()
    @test parse_line_advanced(solution, "don't() mul(2,3)") == 0

    solution = Solution()
    @test parse_line_advanced(solution, "do() mul(2,3) don't() mul(4,5) do() mul(1,1)") == 7

    solution = Solution()
    @test parse_line_advanced(solution, "mul(3,3)") == 9
end

test_solution()



