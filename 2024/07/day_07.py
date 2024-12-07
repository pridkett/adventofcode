from typing import List, Callable, Dict
from dataclasses import dataclass

OperationDict = Dict[str, Callable[[int, int], int]]

OPERATIONS: OperationDict = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y
}

OPERATIONS_CONCAT: OperationDict = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
    '||': lambda x, y: int(str(x) + str(y))
}

@dataclass
class OperatorInput:
    target: int
    values: List[int]

@dataclass
class OperatorOutput:
    operators: List[str]
    target: int
    values: List[int]

class Solution:
    def __init__(self):
        pass
    
    # General Algorithm
    # Recursively iterate on the operators across the values
    # If the value is greater than the target, stop the branch
    # The value is equal to the count, return the set of operators

    def find_operators_recursive(self, target: int, values: List[int], current: int, operator: str, operations: OperationDict) -> List[str]:
        current = operations[operator](current, values[0])
        if current == target and len(values) == 1:
            return [operator]
        if current > target or len(values) == 1:
            return []
        for op in operations.keys():
            result = self.find_operators_recursive(target, values[1:], current, op, operations)
            if result:
                return [operator] + result
        return []
    
        
        
    def find_operators_one(self, input: OperatorInput, operations: OperationDict) -> List[str]:
        for op in operations:
            result = self.find_operators_recursive(input.target, input.values[1:], input.values[0], op, operations)
            if result:
                return result
        return []
    
    def find_operators(self, input: str, operations: OperationDict=OPERATIONS) -> List[OperatorOutput]:
        operators:List[OperatorOutput] = []

        for line in input.splitlines():
            try:
                op_input = OperatorInput(
                    target=int(line.split(":")[0]),
                    values=[int(x) for x in line.split(":")[1].split()]
                )

                ops = self.find_operators_one(op_input, operations)
                operators.append(OperatorOutput(operators=ops, target=op_input.target, values=op_input.values))
            except:
                raise Exception(f"Error processing line: '{line}'")
        return operators
    
    def find_operators_concat(self, input: str) -> List[OperatorOutput]:
        return self.find_operators(input, operations=OPERATIONS_CONCAT)
        
def main(fn: str):
    with open(fn) as f:
        s = Solution()
        data = f.read()
        operators = s.find_operators(data)
        print(sum([x.target for x in operators if x.operators != []]))
        operators = s.find_operators_concat(data)
        print(sum([x.target for x in operators if x.operators != []]))        

if __name__ == "__main__":
    main("input.txt")
