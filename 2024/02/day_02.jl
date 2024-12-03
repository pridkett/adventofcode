mutable struct Solution
    function Solution()
        new()
    end
end

function _evaluate(solution::Solution, numbers::Vector{Int})::Int
    rev = false

    for i in 2:length(numbers)
        if numbers[i] < numbers[i-1]
            rev = true
            break
        end
    end

    sorted = sort(numbers, rev=rev)
    spacing_okay = true

    for i in 2:length(numbers)
        if !(1 <= abs(numbers[i] - numbers[i-1]) <= 3)
            spacing_okay = false
            break
        end
    end

    if (sorted == numbers) && spacing_okay
        return 1
    end

    return 0
end

function evaluate(solution::Solution, line::String)::Tuple{Int, Int}
    numbers = map(x->parse(Int, x), split(line, " "))

    basic = _evaluate(solution, numbers)

    if basic == 1
        return (1, 1)
    end

    for i in eachindex(numbers)
        new_numbers = [numbers[j] for j in eachindex(numbers) if j != i]
        if _evaluate(solution, new_numbers) > 0
            return(0, 1)
        end
    end

    return (0, 0)
end

function read_data(fn::String)::Vector{String}
    return readlines(fn)
end

if abspath(PROGRAM_FILE) == @__FILE__
    data = read_data("input.txt")
    s = Solution()

    results = map(x->evaluate(s, x), data)

    safe = sum(first, results)
    dampened = sum(last, results)

    println(safe)
    println(dampened)
end