using Printf

mutable struct Solution

    rules::Dict{Int, Vector{Int}}
    flat_rules::Dict{Int, Vector{Int}}

    function Solution()
        new(Dict(), Dict())
    end
end


function check_ordering(solution::Solution, ordering::Vector{Int})::Bool
    for i in eachindex(ordering)
        previous_items = ordering[1:(i-1)]
        intersect = [x for x in get(solution.rules, ordering[i], []) if x in previous_items]
        if length(intersect) > 0
            return false
        end
    end
    return true 
end

function reorder(solution::Solution, ordering::Vector{Int})::Vector{Int}
    new_output::Vector{Int} = []
    for i in eachindex(ordering)
        intersect = [x for x in get(solution.rules, ordering[i], []) if x in new_output]
        if length(intersect) > 0
            indices = [findfirst(x->x==y, new_output) for y in intersect]
            new_index = minimum(i for i in indices if i !== nothing)
            insert!(new_output, new_index, ordering[i])
        else
            push!(new_output, ordering[i])
        end
    end
    return new_output
end

function add_rule(solution::Solution, key::Int, val::Int)::Vector{Int}
    if haskey(solution.rules, key)
        push!(solution.rules[key], val)
    else
        solution.rules[key] = [val]
    end
    return solution.rules[key]
end

function do_all(solution::Solution, lines::Vector{String})::Int
    total_sum = 0
    for line in lines
        if occursin("|", line)
            k, v = map(x->parse(Int, x), split(line, "|"))
            add_rule(solution, k, v)
        end
        if occursin(",", line)
            ordering = map(x->parse(Int, x), split(line, ","))
            if check_ordering(solution, ordering)
                middle_index = ceil(Int, length(ordering) / 2)
                total_sum = total_sum + ordering[middle_index]
            end
        end
    end
    return total_sum
end

function do_all_reordering(solution::Solution, lines::Vector{String})::Int
    total_sum = 0
    for line in lines
        if occursin("|", line)
            k, v = map(x->parse(Int, x), split(line, "|"))
            add_rule(solution, k, v)
        end
    end

    for line in lines
        if occursin(",", line)
            ordering = map(x->parse(Int, x), split(line, ","))
            if !check_ordering(solution, ordering)
                new_ordering = reorder(solution, ordering)
                middle_index = ceil(Int, length(new_ordering) / 2)
                total_sum = total_sum + new_ordering[middle_index]
            end
        end
    end
    return total_sum
end

function read_data(fn::String)::Vector{String}
    return readlines(fn)
end

if abspath(PROGRAM_FILE) == @__FILE__
    data = read_data("input.txt")

    s = Solution()
    println(do_all(s, data))

    s = Solution()
    println(do_all_reordering(s, data))
end
