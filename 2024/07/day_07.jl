using Printf

const OperationsDict = Dict{Char, Function}

OPERATIONS::OperationsDict = Dict(
    '+' => (x, y) -> x + y,
    '*' => (x, y) -> x * y
)

OPERATIONS_CONCAT::OperationsDict = Dict(
    '+' => (x, y) -> x + y,
    '*' => (x, y) -> x * y,
    '|' => (x, y) -> parse(Int64, string(x) * string(y))
)

struct OperatorInput
    target::Int64
    values::Vector{Int64}

    function OperatorInput(target, vals)
        new(target, vals)
    end
end

struct OperatorOutput
    operators::Vector{Char}
    target::Int64
    values::Vector{Int64}

    function OperatorOutput(op, target, vals)
        new(op, target, vals)
    end
end

function find_operators_recursive(target::Int64, values::Vector{Int64}, current::Int64, operator::Char, operations::OperationsDict)::Vector{Char}
    current = operations[operator](current, values[1])
    if current == target && length(values) == 1
        return [operator]
    elseif current > target || length(values) == 1
        return []
    end

    for op in keys(operations)
        result = find_operators_recursive(target, values[2:end], current, op, operations)
        if length(result) > 0
            return [operator; result]
        end
    end

    return []
end

function find_operators_one(input::OperatorInput, operations::OperationsDict)::Vector{Char}
    for op in keys(operations)
        result = find_operators_recursive(input.target, input.values[2:end], input.values[1], op, operations)
        if length(result) > 0
            return result
        end
    end
    return []
end

function find_operators(input::Vector{String}, operations::OperationsDict=OPERATIONS)::Vector{OperatorOutput}
    operators::Vector{OperatorOutput} = []

    for line in input
        parts = split(line, ":")
        target = parse(Int64, strip(parts[1]))
        values = [parse(Int64, x) for x in split(strip(parts[2]), " ")]
        op = find_operators_one(OperatorInput(target, values), operations)
        push!(operators, OperatorOutput(op, target, values))
    end

    return operators
end

function find_operators_concat(input::Vector{String})::Vector{OperatorOutput}
    return find_operators(input, OPERATIONS_CONCAT)
end

function read_data(fn::String)::Vector{String}
    return readlines(fn)
end

if abspath(PROGRAM_FILE) == @__FILE__
    data = read_data("input.txt")

    operators = find_operators(data)
    println(sum([x.target for x in operators if x.operators != []]))

    operators = find_operators_concat(data)
    println(sum([x.target for x in operators if x.operators != []]))

end
