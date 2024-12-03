mutable struct Solution
    process_instructions::Bool
    simple_re::Regex
    advanced_re::Regex

    function Solution()
        new(true, r"mul\((\d{1,3}),(\d{1,3})\)", r"(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))")
    end
end


function parse_line(solution::Solution, line::String)::Int
    total = 0
    for match in eachmatch(solution.simple_re, line)
        total += parse(Int, match.captures[1]) * parse(Int, match.captures[2])
    end
    return total
end

function parse_line_advanced(solution::Solution, line::String)::Int
    total = 0
    for match in eachmatch(solution.advanced_re, line)
        if match.captures[4] == "do()"
            solution.process_instructions = true
        elseif match.captures[5] == "don't()"
            solution.process_instructions = false
        elseif !isempty(match.captures[1]) && solution.process_instructions
            total += parse(Int, match.captures[2]) * parse(Int, match.captures[3])
        end
    end
    return total
end

function read_data(fn::String)::Vector{String}
    return readlines(fn)
end

if abspath(PROGRAM_FILE) == @__FILE__
    data = read_data("input.txt")

    sum_basic = map(x->parse_line(Solution(), x), data) |> sum
    s = Solution()
    sum_advanced = map(x->parse_line_advanced(s, x), data) |> sum

    println(sum_basic)
    println(sum_advanced)
end
