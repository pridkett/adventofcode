from typing import List, Dict

INPUT_FILE = "input.txt"

def read_input(fn: str) -> List[List[int]]:
    output:List[List[int]] = []
    with open(fn) as f:
        for line in f:
            parts = [int(x) for x in line.strip().split()]
            for i, j in enumerate(parts):
                if len(output) <= i:
                    output.append([j])
                else:
                    output[i].append(j)
    return output

def run_algorithm(data: List[List[int]]) -> int:
    l1 = data[0]
    l2 = data[1]
    l1.sort()
    l2.sort()

    assert len(l1) == len(l2)

    return sum([abs(x - y) for x, y in zip(l1, l2)])

def run_algorithm2(data: List[List[int]]) -> int:
    l1 = data[0]
    l1.sort()

    h2: Dict[int, int] = {}
    for x in data[1]:
        h2[x] = h2.get(x, 0) + 1

    return sum([x * h2[x] for x in l1 if x in h2])

def main():
    data = read_input(INPUT_FILE)
    output = run_algorithm(data)
    print(f"final output part 1: {output}")
    output2 = run_algorithm2(data)
    print(f"final output part 2: {output2}")

if __name__ == "__main__":
    main()
