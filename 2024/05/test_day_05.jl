using Test
include("./day_05.jl")

# Unit tests
function test_solution()
    solution = Solution()

    add_rule(solution, 1, 2)
    add_rule(solution, 2, 3)
    @test check_ordering(solution, [1, 2, 3]) == true

    solution = Solution()
    add_rule(solution, 3, 2)
    add_rule(solution, 2, 1)
    @test check_ordering(solution, [1, 2, 3]) == false


    rules = [String(strip(x)) for x in split("""47|53
                                                97|13
                                                97|61
                                                97|47
                                                75|29
                                                61|13
                                                75|53
                                                29|13
                                                97|29
                                                53|29
                                                61|53
                                                97|53
                                                61|29
                                                47|13
                                                75|47
                                                97|75                   
                                                47|61
                                                75|61
                                                47|29
                                                75|13
                                                53|13""")]

    orderings = [String(strip(x)) for x in split("""75,47,61,53,29
                                                    97,61,53,29,13
                                                    75,29,13
                                                    75,97,47,61,53
                                                    61,13,29
                                                    97,13,75,29,47""")]
    
    solution = Solution()
    [add_rule(solution, parse(Int, split(x, "|")[1]), parse(Int, split(x, "|")[2])) for x in rules]
    ordering_target = [true, true, true, false, false, false]

    for i in eachindex(orderings)
        ordering = map(x->parse(Int, x), split(orderings[i], ","))
        @test check_ordering(solution, ordering) == ordering_target[i]
    end


    solution = Solution()
    @test do_all(solution, vcat(rules, orderings)) == 143

    solution = Solution()
    @test do_all_reordering(solution, vcat(rules, orderings)) == 123

end

test_solution()