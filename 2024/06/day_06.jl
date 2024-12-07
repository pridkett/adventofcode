using Printf

GUARD_CHARS = ['^', '<', 'v', '>']

mutable struct Solution

    map::Vector{Vector{Char}}
    visit_map::Vector{Vector{Char}}
    map_width::Int
    map_height::Int

    function Solution()
        new([], [], -1, -1)
    end
end


function load_map(solution::Solution, input::Vector{String})
    solution.map = [Vector{Char}(undef, length(input[1])) for _ in 1:length(input)]
    for (i, line) in enumerate(input)
        for (j, char) in enumerate(line)
            solution.map[i][j] = char
        end
    end
    solution.map_width = length(input[1])
    solution.map_height = length(input)
end

function create_visit_map(solution::Solution)
    solution.visit_map = deepcopy(solution.map)

    guard_x = -1
    guard_y = -1
    guard_state = " "

    # find the guard_state
    for y in range(1, solution.map_height)
        for x in range(1, solution.map_width)
            if solution.map[y][x] in GUARD_CHARS
                guard_x = x
                guard_y = y
                guard_state = solution.map[y][x]
                solution.visit_map[guard_y][guard_x] = '.'
                break
            end
        end
        if guard_x != -1
            break
        end
    end

    @assert guard_x != -1 && guard_y != -1 "Unable to find location of guard"

    while true
        solution.visit_map[guard_y][guard_x] = 'X'

        if guard_state == '^'
            if guard_y == 1
                break
            elseif solution.map[guard_y-1][guard_x] == '#'
                guard_state = '>'
            else
                guard_y = guard_y - 1
            end
        elseif guard_state == '>'
            if guard_x == solution.map_width
                break
            elseif solution.map[guard_y][guard_x + 1] == '#'
                guard_state = 'v'
            else
                guard_x = guard_x + 1
            end
        elseif guard_state == 'v'
            if guard_y == solution.map_height
                break
            elseif solution.map[guard_y + 1][guard_x] == '#'
                guard_state = '<'
            else
                guard_y = guard_y + 1
            end
        elseif guard_state == '<'
            if guard_x == 1
                break
            elseif solution.map[guard_y][guard_x - 1] == '#'
                guard_state = '^'
            else
                guard_x = guard_x - 1
            end
        end
    end
end

function count_distinct_positions(solution::Solution)::Int
    count = 0
    for y in range(1, solution.map_height)
        for x in range(1, solution.map_width)
            if solution.visit_map[y][x] == 'X'
                count = count + 1
            end
        end
    end
    return count
end

function place_obstacles(solution::Solution)::Vector{Tuple{Int, Int}}
    start_guard_x = -1
    start_guard_y = -1
    start_guard_state = " "
    for y in eachindex(solution.map)
        for x in eachindex(solution.map[y])
            if solution.map[y][x] in GUARD_CHARS
                start_guard_x = x
                start_guard_y = y
                start_guard_state = solution.map[y][x]
                break
            end
        end
        if start_guard_x != -1
            break
        end
    end

    @assert start_guard_x != -1 && start_guard_y != -1 "Unable to find location of guard"
    obstacle_locations = Vector{Tuple{Int, Int}}()

    create_visit_map(solution)

    for (x, y) in [(x,y) for x in range(1, solution.map_width) for y in range(1, solution.map_height)]
        if solution.visit_map[y][x] != 'X'
            continue
        end

        obstacle_visit_map = [Dict{Char, Bool}() for _ in 1:solution.map_width, _ in 1:solution.map_height]
        guard_x = start_guard_x
        guard_y = start_guard_y
        guard_state = start_guard_state

        while true
            if haskey(obstacle_visit_map[guard_x,guard_y], guard_state)
                push!(obstacle_locations, (x, y))
                break
            end
            obstacle_visit_map[guard_x,guard_y][guard_state] = true
            # print("($guard_x, $guard_y)=$(obstacle_visit_map[guard_x,guard_y]) ")
            if guard_state == '^'
                if guard_y == 1
                    break
                elseif solution.map[guard_y-1][guard_x] == '#' || (guard_x == x && guard_y-1 == y)
                    guard_state = '>'
                else
                    guard_y = guard_y - 1
                end
            elseif guard_state == '>'
                if guard_x == solution.map_width
                    break
                elseif solution.map[guard_y][guard_x + 1] == '#' || (guard_x+1 == x && guard_y == y)
                    guard_state = 'v'
                else
                    guard_x = guard_x + 1
                end
            elseif guard_state == 'v'
                if guard_y == solution.map_height
                    break
                elseif solution.map[guard_y + 1][guard_x] == '#' || (guard_x == x && guard_y+1 == y)
                    guard_state = '<'
                else
                    guard_y = guard_y + 1
                end
            elseif guard_state == '<'
                if guard_x == 1
                    break
                elseif solution.map[guard_y][guard_x - 1] == '#' || (guard_x-1 == x && guard_y == y)
                    guard_state = '^'
                else
                    guard_x = guard_x - 1
                end
            end
        end
    end
    return obstacle_locations
end

function read_data(fn::String)::Vector{String}
    return readlines(fn)
end

if abspath(PROGRAM_FILE) == @__FILE__
    data = read_data("input.txt")

    s = Solution()
    load_map(s, data)
    create_visit_map(s)
    println(count_distinct_positions(s))

    s = Solution()
    load_map(s, data)
    obstacles = place_obstacles(s)
    println(length(obstacles))
end
