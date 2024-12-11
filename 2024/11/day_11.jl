using Printf

struct Solution
    stones::Vector{Int64}

    function Solution(input::String)
        stones = [parse(Int, c) for c in split(input, " ")]
        new(stones)
    end
end

function process_stone(stone::Int64)::Vector{Int64}
    if stone == 0
        return [1]
    end
    if length(string(stone)) % 2 == 0
        stone_str = string(stone)
        stone_len = length(stone_str)
        return [parse(Int64, stone_str[1:div(stone_len, 2)]), parse(Int64, stone_str[div(stone_len,2)+1:end])]
    end
    return [stone*2024]
end

function multi_blink(s::Solution, n::Int64)::Int64
    stone_map::Dict{Int64, Int64} = Dict()
    for i in eachindex(s.stones)
        if !haskey(stone_map, s.stones[i])
            stone_map[s.stones[i]] = 0
        end
        stone_map[s.stones[i]] += 1
    end

    for i in 1:n
        # println("Start ", i, ": ", stone_map)

        new_map::Dict{Int64, Int64} = Dict()
        for (stone, count) in stone_map
            new_stones = process_stone(stone)
            for new_stone in new_stones
                if !haskey(new_map, new_stone)
                    new_map[new_stone] = 0
                end
                new_map[new_stone] += count
            end
            stone_map = new_map
        end
        # println("End ", i, ": ", stone_map)
    end
    return sum(values(stone_map))
end

function read_data(fn::String)::String
    return read(fn, String)
end

if abspath(PROGRAM_FILE) == @__FILE__
    data = read_data("input.txt")
    s = Solution(data)
    println(multi_blink(s, 25))
    println(multi_blink(s, 75))
end
