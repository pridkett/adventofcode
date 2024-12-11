from typing import List, Iterable, Tuple
import numpy as np
import time
import numpy.typing as npt
from collections import deque, defaultdict

class Solution:
    def __init__(self):
        self.stones:List[int] = []

    def load(self, input:str):
        self.stones = list(map(int, input.split()))

    # a different implementation that focuses on each individual stone...
    def multi_blink(self, n:int, round:int=1) -> int:
        d = deque([(x, 0) for x in self.stones])
        i = 0
        while len(d) > 0:
            avg_n = 0
            # if i % 1000 == 0:
            #     print(f"round:{round} stone {i}/{len(d)} {i/len(d)*100:.2f}% avg_n={avg_n/1000}")
            #     avg_n = 0
            stone = d.popleft()
            ctr = stone[1]
            prepend_nodes = deque()
            while stone[1] < n:
                avg_n = avg_n + stone[1]
                new_stones = [(x, ctr + 1) for x in self._process_stone(stone[0])]
                stone = new_stones[0]
                if len(new_stones) == 2:
                    prepend_nodes.appendleft(new_stones[1])
                    # d.appendleft(new_stones[1])
                ctr = ctr + 1
            d.extendleft(prepend_nodes)
            i = i +1
        return i

    def multi_blink2(self, n:int, round:int=1) -> int:
        d:defaultdict[int,int] = defaultdict(lambda: 0)
        for i, stone in enumerate(self.stones):
            d[stone] = d[stone] + 1

        for i in range(n):
            new_d:defaultdict[int,int] = defaultdict(lambda: 0)
            print(f"round {i}: {len(d)} keys")
            for k, v in d.items():
                new_stones = self._process_stone(k)
                for ns in new_stones:
                    new_d[ns] = new_d[ns] + v
            d = new_d
        return sum(d.values())
    
    def blink(self, n:int):
        for i in range(n):
            start_time = time.time()
            new_stones = [item for sublist in [self._process_stone(x) for x in self.stones] for item in sublist]
            self.stones = new_stones
            end_time = time.time()
            print(f"Iteration {i+1}/{n} took {end_time - start_time:.4f} seconds - {self.num_stones()} stones")

    def num_stones(self) -> int:
        return len(self.stones)
    
    def _process_stone(self, stone:int) -> List[int]:
        if stone == 0:
            return [1]
        if len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            return [int(stone_str[:len(stone_str)//2]), int(stone_str[len(stone_str)//2:])]
        else:
            return [stone*2024]
        
    def to_string(self) -> str:
        return " ".join(map(str, self.stones))

def main(fn: str):
    with open(fn) as f:
        s = Solution()
        data = f.read().strip()
        s.load(data)
        t1 = time.time()
        s.blink(25)
        t2 = time.time()
        print(f"blink took {t2-t1:.4f} seconds")
        print (s.num_stones())
        s.load(data)
        d = s.multi_blink2(75)
        t2 = time.time()
        print(f"multi_blink took {t2-t1:.4f} seconds")
        print(d)

if __name__ == "__main__":
    main("input.txt")
