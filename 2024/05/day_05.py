from typing import List, Dict, Set, Optional

class Solution:
    def __init__(self):
        self.rules:Dict[int, List[int]] = {}

    def check_ordering(self, ordering: List[int]) -> bool:
        for i in range(len(ordering)):
            previous_items = ordering[:i]
            intersect = [x for x in self.rules.get(ordering[i], []) if x in previous_items]
            if len(intersect) > 0:
                return False
        return True
    
    def reorder(self, ordering: List[int]) -> List[int]:
        new_output: List[int] = []
        for i in range(len(ordering)):
            previous_items = new_output[:i]
            intersect = set([x for x in self.rules.get(ordering[i], []) if x in previous_items])
            if len(intersect) > 0:
                # find the earliest index of any element in the index list
                index = min([new_output.index(x) for x in intersect])
                new_output.insert(index, ordering[i])
            else:
                new_output.append(ordering[i])
        return new_output
    
    def add_rule(self, key: int, val: int) -> List[int]:
        if key in self.rules:
            self.rules[key].append(val)
        else:
            self.rules[key] = [val]
        return self.rules[key]
        
    def do_all(self, input: str) -> int:
        total_sum = 0
        for line in input.splitlines():
            if "|" in line:
                k, v = [int(x) for x in line.split("|")]
                self.add_rule(k, v)
            if "," in line:
                ordering = [int(x) for x in line.split(",")]
                if self.check_ordering(ordering):
                    total_sum = total_sum + ordering[len(ordering)//2]
        return total_sum

    def do_all_reordering(self, input: str) -> int:
        total_sum = 0
        for line in input.splitlines():
            if "|" in line:
                k, v = [int(x) for x in line.split("|")]
                self.add_rule(k, v)
        
        for line in input.splitlines():
            if "," in line:
                ordering = [int(x) for x in line.split(",")]
                if not(self.check_ordering(ordering)):
                    new_ordering = self.reorder(ordering)
                    total_sum = total_sum + new_ordering[len(new_ordering)//2]
        return total_sum

    
def main(fn: str):
    with open(fn) as f:
        s = Solution()
        data = f.read()
        print(s.do_all(data))
        s2 = Solution()
        print(s2.do_all_reordering(data))
    
if __name__ == "__main__":
    main("input.txt")
