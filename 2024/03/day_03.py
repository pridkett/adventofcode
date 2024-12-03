import re

process_instructions = True

class Solution:
    def __init__(self):
        self.process_instructions = True
        self.simple_re = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
        self.advanced_re = re.compile(r"(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))")

    def parse_line(self, line: str) -> int:
        matches = self.simple_re.findall(line)
        sum = 0
        for match in matches:
            sum = sum + int(match[0]) * int(match[1])
        return sum

    def parse_line_advanced(self, line: str) -> int:
        matches = self.advanced_re.findall(line)
        sum = 0
        for match in matches:
            if match[3] != "":
                self.process_instructions = True
            if match[4] != "":
                self.process_instructions = False
            if match[0] != "" and self.process_instructions:
                sum = sum + int(match[1]) * int(match[2])
        return sum


def main(fn: str):
    s = Solution()
    with open(fn) as f:
        lines = f.readlines()
        print(sum([s.parse_line(line) for line in lines]))
        print(sum([s.parse_line_advanced(line) for line in lines]))


# parse_line("?,'mul(268,621)why() mul(668,915)mul(887,633)")
if __name__ == "__main__":
    main("input.txt")

# parse_line_advanced("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
# previous answers
# part 2: 101681733 - too high
# part 2: 100189366 - correct - misread the problem statement that do() and don't() affect state across lines
