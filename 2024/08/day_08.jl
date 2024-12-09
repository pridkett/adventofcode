using Printf


const AntennaDict = Dict{Char, Vector{Tuple{Int64, Int64}}}
const AntinodeDict = Set{Tuple{Int64, Int64}}


mutable struct Solution
    map::AbstractMatrix{Char}
    antennas::AntennaDict
    antinodes::AntinodeDict
    resonant_antinodes::AntinodeDict
    width::Int64
    height::Int64

    function Solution(map)
        antennas = AntennaDict()
        antinodes = AntinodeDict()
        resonant_antinodes = AntinodeDict()
        dims = size(map)
        new(map, antennas, antinodes, resonant_antinodes, dims[1], dims[2])
    end
end

function parse_input(input::String)::Solution
    lines = [strip(x) for x in split(input, "\n") if !isempty(strip(x))]
    height = length(lines)
    width = maximum(length(line) for line in lines)
    matrix = fill(' ', height, width)
    for (i, line) in enumerate(lines)
        for (j, char) in enumerate(strip(line))
            matrix[i, j] = char
        end
    end
    return Solution(matrix)
end

function find_antenna_locations(solution::Solution)::AntennaDict
    antennas = AntennaDict()
    for y in 1:solution.height
        for x in 1:solution.width
            if solution.map[y, x] ∉ ['#', '.']
                antennas[solution.map[y, x]] = [get(antennas, solution.map[y, x], Vector{Tuple{Int64, Int64}}()); [(y, x)]]
            end
        end
    end
    solution.antennas = antennas
    return antennas
end

function find_antinode_locations(solution::Solution)::AntinodeDict
    antinodes = AntinodeDict()
    for antenna_id in keys(solution.antennas)
        locations = solution.antennas[antenna_id]
        for i in eachindex(locations)
            node1 = locations[i]
            for j in  range(i+1, length(locations))
                node2 = locations[j]
                y_diff = node2[1] - node1[1]
                x_diff = node2[2] - node1[2]
                    
                antenna1 = (node1[1] - y_diff, node1[2] - x_diff)
                antenna2 = (node2[1] + y_diff, node2[2] + x_diff)
                if 0 < antenna1[1] <= solution.height && 0 < antenna1[2] <= solution.width
                    push!(antinodes, antenna1)
                end
                if 0 < antenna2[1] <= solution.height && 0 < antenna2[2] <= solution.width
                    push!(antinodes, antenna2)
                end
            end
        end
    end
    solution.antinodes = antinodes
    return antinodes
end

function find_resonant_antinode_locations(solution::Solution)::AntinodeDict
    resonant_antinodes = AntinodeDict()
    for antenna_id in keys(solution.antennas)
        locations = solution.antennas[antenna_id]
        for i in eachindex(locations)
            node1 = locations[i]
            for j in  range(i+1, length(locations))
                node2 = locations[j]
                y_diff = node2[1] - node1[1]
                x_diff = node2[2] - node1[2]
                
                mult_factor = 0
                while true
                    antenna1 = (node1[1] - y_diff*mult_factor, node1[2] - x_diff*mult_factor)
                    if 0 < antenna1[1] <= solution.height && 0 < antenna1[2] <= solution.width
                        push!(resonant_antinodes, antenna1)
                    else
                        break
                    end
                    mult_factor += 1
                end
    
                mult_factor = 0
                while true
                    antenna2 = (node2[1] + y_diff*mult_factor, node2[2] + x_diff*mult_factor)
                    if 0 < antenna2[1] <= solution.height && 0 < antenna2[2] <= solution.width
                        push!(resonant_antinodes, antenna2)
                    else
                        break
                    end
                    mult_factor += 1
                end
            end
        end
    end
    solution.resonant_antinodes = resonant_antinodes
    return resonant_antinodes
end

function read_data(fn::String)::String
    return read(fn, String)
end

if abspath(PROGRAM_FILE) == @__FILE__
    data = read_data("input.txt")
    solution = parse_input(data)
    antennas = find_antenna_locations(solution)
    antinodes = find_antinode_locations(solution)
    resonant_antinodes = find_resonant_antinode_locations(solution)

    println(length(antinodes))
    println(length(resonant_antinodes))
end
