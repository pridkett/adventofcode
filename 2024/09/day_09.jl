using Printf

MISSING_VAL = -1

const DiskMapVector = Vector{Int64}

mutable struct Solution
    original_input::String
    disk_map::DiskMapVector
    optimized_disk_map::DiskMapVector
    unfragmented_disk_map::DiskMapVector
    total_blocks::Int64

    function Solution(input::String)
        disk_nums = [parse(Int, c) for c in input if c != '\n']
        disk_map = DiskMapVector()
        for i in eachindex(disk_nums)
            if i%2 == 0
                push!(disk_map, fill(MISSING_VAL, disk_nums[i])...)
            else
                push!(disk_map, fill(div(i-1,2), disk_nums[i])...)
            end
        end

        optimized_disk_map = copy(disk_map)
        unfragmented_disk_map = copy(disk_map)
        total_blocks = length(disk_map)
        new(input, disk_map, optimized_disk_map, unfragmented_disk_map, total_blocks)
    end
end

function optimize_disk_map(s::Solution)::DiskMapVector
    end_ctr = s.total_blocks
    for i in 1:s.total_blocks
        if s.optimized_disk_map[i] == MISSING_VAL
            while s.optimized_disk_map[end_ctr] == MISSING_VAL
                end_ctr -= 1
            end
            if i >=  end_ctr
                break
            end
            s.optimized_disk_map[i] = s.optimized_disk_map[end_ctr]
            s.optimized_disk_map[end_ctr] = MISSING_VAL


        end
    end
    return s.optimized_disk_map
end

function unfragment_disk_map(s::Solution)::DiskMapVector
    number_map = [parse(Int, c) for c in s.original_input if c != '\n']
    freespace_map = Dict{Int64, Vector{Tuple{Int64, Int64}}}()
    block_ctr = 0
    for i in eachindex(number_map)
        # remember, Julia uses 1-based indexing
        if i%2 == 0 && number_map[i] != 0
            if !haskey(freespace_map, number_map[i])
                freespace_map[number_map[i]] = []
            end
            push!(freespace_map[number_map[i]], (block_ctr+1, block_ctr + number_map[i]))
        end
        block_ctr = block_ctr + number_map[i]
    end

    i = length(s.disk_map)
    min_moved_val = maximum(s.unfragmented_disk_map)+1
    while true
        if i == 0
            break
        end
        start = missing
        stop = missing
        val = missing
        if s.unfragmented_disk_map[i] != MISSING_VAL && s.unfragmented_disk_map[i] < min_moved_val
            val = s.unfragmented_disk_map[i]
            min_moved_val = val
            if val == 0
                break
            end
            stop = i
            start = i
            while s.disk_map[i] == val
                start = i
                i = i - 1
            end
            file_length = stop - start + 1

            key_vals = sort(collect(filter(x -> x >= file_length, keys(freespace_map))))
            if length(key_vals) > 0
                best_fit = findmin(freespace_map[key_vals[1]])
                best_fit_key = key_vals[1]
                for k in key_vals
                    fit = findmin(freespace_map[k])
                    if fit[1] < best_fit[1]
                        best_fit = fit
                        best_fit_key = k
                    end
                end

                # don't move files backward
                if best_fit[1][1] < start
                    # move the file
                    for j in 1:file_length
                        s.unfragmented_disk_map[best_fit[1][1] + j - 1] = val
                        s.unfragmented_disk_map[start + j - 1] = -1
                    end

                    # update the freespace map
                    if best_fit_key > file_length
                        new_start = best_fit[1][1] + file_length - 1
                        new_stop = best_fit[1][2]
                        new_length = best_fit_key - file_length
                        if !haskey(freespace_map, new_length)
                            freespace_map[new_length] = []
                        end
                        push!(freespace_map[new_length], (new_start+1, new_stop))
                    end

                    # remove the old freespace
                    deleteat!(freespace_map[best_fit_key], best_fit[2])
                    if length(freespace_map[best_fit_key]) == 0
                        delete!(freespace_map, best_fit_key)
                    end

                    # create the new freespace
                    if !haskey(freespace_map, file_length)
                        freespace_map[file_length] = []
                    end
                    push!(freespace_map[file_length], (start, start + file_length - 1))

                    
                    # consolidate the freespace where the file was
                    # check at the start
                    if start > 1 && s.unfragmented_disk_map[start - 1] == -1 
                        # find the element in freespace_map with element 2 == start-1
                        key = [k for k in keys(freespace_map) if any([x[2] == start-1 for x in freespace_map[k]])]
                        if key != []
                            # find the element in freespace_map[key] with element 2 == start-1
                            idx = findfirst([x[2] == start-1 for x in freespace_map[key[1]]])
                            if idx != nothing
                                new_start = freespace_map[key[1]][idx][1]
                                new_stop = start + file_length - 1
                                deleteat!(freespace_map[key[1]], idx)
                                pop!(freespace_map[file_length])
                                if length(freespace_map[key[1]]) == 0
                                    delete!(freespace_map, key[1])
                                end

                                start = new_start
                                stop = new_stop
                                file_length = new_stop - new_start + 1
                                if !haskey(freespace_map, file_length)
                                    freespace_map[file_length] = []
                                end
                                push!(freespace_map[file_length], (start, stop))
                            end
                        end
                    end

                    # check to consolidate free space at the end
                    # this actually isn't needed to get the right answer...
                    if start + file_length <= length(s.unfragmented_disk_map) && s.unfragmented_disk_map[start + file_length] == -1
                    end
                end
            end
        else
            i = i - 1
        end  
    end
    return s.unfragmented_disk_map
end

function disk_map_to_string(s::Solution)::String
    return join([c == -1 ? '.' : string(c) for c in s.disk_map], "")
end

function optimized_disk_map_to_string(s::Solution)::String
    return join([c == -1 ? '.' : string(c) for c in s.optimized_disk_map], "")
end

function unfragmented_disk_map_to_string(s::Solution)::String
    return join([c == -1 ? '.' : string(c) for c in s.unfragmented_disk_map], "")
end

function checksum_disk_map(s::Solution)::Int64
    return sum([s.optimized_disk_map[i]*(i-1) for i in eachindex(s.optimized_disk_map) if s.optimized_disk_map[i] != MISSING_VAL])
end

function unfragmented_checksum_disk_map(s::Solution)::Int64
    return sum([s.unfragmented_disk_map[i]*(i-1) for i in eachindex(s.unfragmented_disk_map) if s.unfragmented_disk_map[i] != MISSING_VAL])
end

function read_data(fn::String)::String
    return read(fn, String)
end

if abspath(PROGRAM_FILE) == @__FILE__
    data = read_data("input.txt")
    solution = Solution(data)
    optimize_disk_map(solution)
    println(checksum_disk_map(solution))
    unfragment_disk_map(solution)
    println(unfragmented_checksum_disk_map(solution))
end
