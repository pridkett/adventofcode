using Printf

mutable struct Solution
    function Solution()
        new()
    end
end


# function matrix_search(solution::Solution, matrix::[Vector[Char]], search_dirs::Vector{Vector{Tuple(Int, Int)}}, word::String)::Int
function matrix_search(solution::Solution, matrix::Vector{Vector{Char}}, search_dirs::Vector{Vector{Tuple{Int, Int}}}, word::String)::Int
    matrix_x = length(matrix[1])
    matrix_y = length(matrix)
    count = 0
    for i in eachindex(search_dirs)
        success = true
        for j in eachindex(word)
            if search_dirs[i][j][1] < 1 || search_dirs[i][j][1] > matrix_x || search_dirs[i][j][2] < 1 || search_dirs[i][j][2] > matrix_y
                success = false
                break
            end
            if matrix[search_dirs[i][j][2]][search_dirs[i][j][1]] != word[j]
                success = false
                break
            end
        end
        if success
            count = count + 1
        end
    end
    return count
end

function find_words(solution::Solution, lines::Vector{String}, word::String)::Int
    total = 0
    matrix = [Vector{Char}(undef, length(lines[1])) for _ in 1:length(lines)]
    for (i, line) in enumerate(lines)
        for (j, char) in enumerate(line)
            matrix[i][j] = char
        end
    end

    # Perform a matrix search for the word
    for i in 1:length(matrix)
        for j in 1:length(matrix[1])
            if matrix[i][j] == word[1]
                # create a set of arrays of coordinates to search
                search_dirs = [Vector{Tuple{Int, Int}}(undef, length(word)-1) for _ in 1:8]
                for k in 1:length(word)-1
                    # we store (x,y) coordinates
                    search_dirs[1][k] = (j+k, i) # right
                    search_dirs[2][k] = (j-k, i) # left
                    search_dirs[3][k] = (j, i+k) # down
                    search_dirs[4][k] = (j, i-k) # up
                    search_dirs[5][k] = (j+k, i+k) # down-right
                    search_dirs[6][k] = (j-k, i-k) # up-left
                    search_dirs[7][k] = (j-k, i+k) # down-left
                    search_dirs[8][k] = (j+k, i-k) # up-right
                end

                total = total + matrix_search(solution, matrix, search_dirs, word[2:end])
            end
        end
    end
    return total
end

function find_words_x(solution::Solution, lines::Vector{String}, word::String)::Int
    if length(word)%2 != 1
        throw(ArgumentError("The length of the word must be odd"))
    end

    total = 0
    matrix = [Vector{Char}(undef, length(lines[1])) for _ in 1:length(lines)]
    for (i, line) in enumerate(lines)
        for (j, char) in enumerate(line)
            matrix[i][j] = char
        end
    end


    center_letter = word[Int((length(word)+1)/2)]
    start_offset = Int((length(word)-1)/2)
    # Perform a matrix search for the word
    for i in 1:length(matrix)
        for j in 1:length(matrix[1])
            if matrix[i][j] == center_letter
                # create a set of arrays of coordinates to search
                search_dirs1 = [Vector{Tuple{Int, Int}}(undef, length(word)) for _ in 1:2]
                search_dirs2 = [Vector{Tuple{Int, Int}}(undef, length(word)) for _ in 1:2]
                for k in 1:length(word)
                    # we store (x,y) coordinates in two sets - this allows for word to be a palindrome
                    search_dirs1[1][k] = (j+(k-1-start_offset), i+(k-1-start_offset)) # down-right
                    search_dirs1[2][k] = (j-(k-1-start_offset), i-(k-1-start_offset)) # up-left

                    search_dirs2[1][k] = (j+(k-1-start_offset), i-(k-1-start_offset)) # up-right
                    search_dirs2[2][k] = (j-(k-1-start_offset), i+(k-1-start_offset)) # down-left
                end

                if matrix_search(solution, matrix, search_dirs1, word) > 0 &&
                   matrix_search(solution, matrix, search_dirs2, word) > 0
                    total = total + 1
                end
            end
        end
    end
    return total
end

function read_data(fn::String)::Vector{String}
    return readlines(fn)
end

if abspath(PROGRAM_FILE) == @__FILE__
    data = read_data("input.txt")

    s = Solution()
    basic_words = find_words(s, data, "XMAS")
    x_words = find_words_x(s, data, "MAS")
    
    println(basic_words)
    println(x_words)
end
