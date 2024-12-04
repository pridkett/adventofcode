using Test
include("./day_04.jl")

# Unit tests
function test_solution()
    solution = Solution()

    @test find_words(solution, [String(strip(x)) for x in split("""SSXMAS
                                                                   SAMXMS""", "\n")], "XMAS") == 2
    @test find_words(solution, [String(strip(x)) for x in split("""....XXMAS.
                                                                   .SAMXMS...
                                                                   ...S..A...
                                                                   ..A.A.MS.X
                                                                   XMASAMX.MM
                                                                   X.....XA.A
                                                                   S.S.S.S.SS
                                                                   .A.A.A.A.A
                                                                   ..M.M.M.MM
                                                                   .X.X.XMASX""", "\n")], "XMAS") == 18
    @test find_words(solution, [String(strip(x)) for x in split("""XZZS
                                                                   ZMAZ
                                                                   ZMAZ
                                                                   XZZS""", "\n")], "XMAS") == 2
    @test find_words_x(solution, [String(strip(x)) for x in split("""M.S
                                                                     .A.
                                                                     M.S""", "\n")], "MAS") == 1
    @test find_words_x(solution, [String(strip(x)) for x in split("""S.M
                                                                     .A.
                                                                     S.M""", "\n")], "MAS") == 1
    @test find_words_x(solution, [String(strip(x)) for x in split("""M.M
                                                                     .A.
                                                                     S.S""", "\n")], "MAS") == 1
    @test find_words_x(solution, [String(strip(x)) for x in split("""S.M
                                                                     .A.
                                                                     M.S""", "\n")], "MAS") == 0

                                                                     
    @test find_words_x(solution, [String(strip(x)) for x in split(""".M.S......
                                                                     ..A..MSMS.
                                                                     .M.S.MAA..""", "\n")], "MAS") == 1

    @test find_words_x(solution, [String(strip(x)) for x in split("""AMASAAAAAA
                                                                     A.A..MSMS.
                                                                     .M.S.MAA..""", "\n")], "MAS") == 1

    @test find_words_x(solution, [String(strip(x)) for x in split("""AMASAAAAAA
                                                                     AAAAAMSMSA
                                                                     AMASAMAAAA
                                                                     AAAAASMSMA
                                                                     AMASAMAAAA
                                                                     AAAAAAAAAA""", "\n")], "MAS") == 5

    @test find_words_x(solution, [String(strip(x)) for x in split(""".M.S......
                                                                     ..A..MSMS.
                                                                     .M.S.MAA..
                                                                     ..A.ASMSM.
                                                                     .M.S.M....
                                                                     ..........
                                                                     S.S.S.S.S.
                                                                     .A.A.A.A..
                                                                     M.M.M.M.M.
                                                                     ..........""", "\n")], "MAS") == 9
end

test_solution()