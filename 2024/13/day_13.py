from typing import List, TypeAlias, Tuple

ButtonSolveTuple:TypeAlias = Tuple[int, int, int]
A_COST = 3
B_COST = 1
PART_2_MOD = 10000000000000

class Solution:
    def __init__(self):
        pass

    def load(self, input:str, prob_mod:int = 0) -> ButtonSolveTuple:
        lines = [x.strip() for x in input.splitlines()]
        button_a = lines[0].split()
        button_b = lines[1].split()
        prize = lines[2].split()
        target_x = int(prize[1].split('=')[1].split(',')[0]) + prob_mod
        target_y = int(prize[2].split('=')[1]) + prob_mod
        
        x_a = int(button_a[2].split('+')[1].split(',')[0])
        y_a = int(button_a[3].split('+')[1])
        
        x_b = int(button_b[2].split('+')[1].split(',')[0])
        y_b = int(button_b[3].split('+')[1])

        max_iter = 100
        if prob_mod != 0:
            max_iter = prob_mod
        for i in range(max_iter):
            need_x = target_x - i*x_a
            need_y = target_y - i*y_a

            if need_x % x_b == 0 and need_y % y_b == 0 and need_x // x_b == need_y // y_b:
                a_presses = i
                b_presses = need_x // x_b
                return A_COST * a_presses + B_COST * b_presses, i, b_presses
        return -1, -1, -1

    def load_algebra(self, input:str, prob_mod:int=0) -> ButtonSolveTuple:
        lines = [x.strip() for x in input.splitlines()]
        button_a = lines[0].split()
        button_b = lines[1].split()
        prize = lines[2].split()
        target_x = int(prize[1].split('=')[1].split(',')[0]) + prob_mod
        target_y = int(prize[2].split('=')[1]) + prob_mod
        
        x_a = int(button_a[2].split('+')[1].split(',')[0])
        y_a = int(button_a[3].split('+')[1])
        
        x_b = int(button_b[2].split('+')[1].split(',')[0])
        y_b = int(button_b[3].split('+')[1])

        # math class is really tough...let's go shopping
        # this is really a case of solving two sets of equations for a and b
        # and then making sure they're integers
        a_presses, remainder = divmod(target_x * y_b - target_y * x_b, x_a * y_b - y_a * x_b)
        if remainder:
            return -1, -1, -1

        b_presses, remainder = divmod(target_x - x_a * a_presses, x_b)
        if remainder:
            return -1, -1, -1

        return A_COST * a_presses + B_COST * b_presses, a_presses, b_presses


    def process_file(self, input: str) -> Tuple[int, int]:
        current_buffer:List[str] = []
        current_sum = 0
        part2_sum = 0
        for line in [x.strip() for x in input.splitlines()]:
            if line == "":
                result = self.load("\n".join(current_buffer))
                result_2 = self.load_algebra("\n".join(current_buffer), PART_2_MOD)
                current_buffer = []
                if result[0] != -1:
                    current_sum = current_sum + result[0]
                if result_2[0] != -1:
                    part2_sum = part2_sum + result_2[0]
            else:
                current_buffer.append(line)
        if current_buffer != []:
            result = self.load("\n".join(current_buffer))
            result_2 = self.load_algebra("\n".join(current_buffer), PART_2_MOD)
            if result[0] != -1:
                current_sum = current_sum + result[0]
            if result_2[0] != -1:
                part2_sum = part2_sum + result_2[0]

        return current_sum, part2_sum

def main(fn: str):
    with open(fn) as f:
        s = Solution()
        data = f.read()
        print(s.process_file(data))

if __name__ == "__main__":
    main("input.txt")

# guesses:
# 25437 - too low
# 25629 - was accidentally subtracting the -1 for unsolvable problems before

