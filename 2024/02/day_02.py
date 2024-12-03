import argparse
from typing import Tuple, List

def _evaluate(rep: List[int]) -> int:
    asc = rep[1] > rep[0]

    if rep[0] == rep[1]:
        return 0
    
    last_elem = rep[0]

    for elem in rep[1:]:
        if asc and (elem <= last_elem or elem - last_elem > 3):
            return 0
        elif not asc and (elem >= last_elem or last_elem - elem> 3):
            return 0
        last_elem = elem
    return 1

def evaluate_new(report: str) -> Tuple[int, int]:
    rep = [int(x) for x in report.strip().split()]
    rv1 =  _evaluate(rep)
    if rv1 == 1:
        return (1,1)

    # brute force this
    rv2 = min(sum([_evaluate(rep[:x]+rep[x+1:]) for x in range(0, len(rep))]), 1)
    return rv1, rv2


def main(fn: str):
    with open(fn) as f:
        data = f.readlines()
    
    safe = 0
    dampened = 0
    for line in data:
        s, d = evaluate_new(line)
        safe = safe + s
        dampened = dampened + d
    print(f"there are {safe} safe reports")
    print(f"there are {dampened} safe dampened reports")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str)
    args = parser.parse_args()

    main(fn=args.input_file)