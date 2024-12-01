function read_data(fn::String)::Array{Int64,2}
    lines = readlines(fn)
    first_numbers = []
    second_numbers = []

    for line in lines
        numbers = split(line)
        push!(first_numbers, parse(Int64, numbers[1]))
        push!(second_numbers, parse(Int64, numbers[2]))
    end

    first_numbers_sorted = sort(first_numbers)
    second_numbers_sorted = sort(second_numbers)

    return hcat(first_numbers_sorted, second_numbers_sorted)
end

function run_algorithm1(data::Array{Int64,2})::Int64
    l1 = data[:, 1]
    l2 = data[:, 2]
    
    @assert length(l1) == length(l2) "Lengths of l1 and l2 are not equal"

    sum = 0
    
    for i in 1:length(l1)
        sum += abs(l1[i] - l2[i])
    end

    return sum
end

function run_algorithm2(data::Array{Int64,2})::Int64
    l1 = data[:,1]
    l2 = data[:,2]

    @assert length(l1) == length(l2) "Lengths of l1 and l2 are not equal"

    freq_map = Dict{Int64, Int64}()
    for num in l2
        if haskey(freq_map, num)
            freq_map[num] += 1
        else
            freq_map[num] = 1
        end
    end

    sum = 0

    for i in 1:length(l2)
        if haskey(freq_map, l1[i])
            sum = sum + l1[i] * freq_map[l1[i]]
        end
    end
    return sum
end

data = read_data("input.txt")
println(run_algorithm1(data))
println(run_algorithm2(data))
