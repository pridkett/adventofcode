from typing import List, Iterable, Tuple
import numpy as np
import time
import numpy.typing as npt
from collections import deque, defaultdict

GardenMapArray = npt.NDArray[np.int8]
VisitMapArray = npt.NDArray[np.bool_]
GardenGroup = Tuple[int, int, int, int]
SideMap = Tuple[int, int, int, int]

class Solution:
    def __init__(self):
        self.garden_map: GardenMapArray = np.array([])
        self.visit_map: VisitMapArray = np.array([])

    def load(self, input:str):
        self.garden_map = np.array([[ord(x) for x in line.strip()] for line in input.splitlines()], dtype=np.int8)
        self.visit_map = np.zeros(self.garden_map.shape, dtype=np.bool_)

    def _is_same(self, y:int, x:int, value:int) -> bool:
        return 0 <= x < self.garden_map.shape[1] and 0 <= y < self.garden_map.shape[0] and self.garden_map[y, x] == value
    
    def visit_group(self, y:int, x:int, value:int) -> GardenGroup:
        # lets be fancy, and not use recurision
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque([(y, x)])
        sideq = deque([(y, x)])
        group_size = 0
        group_perimiter = 0
        sides = 0
        while q:
            y, x = q.popleft()
            if self.visit_map[y, x]:
                continue
            self.visit_map[y, x] = True
            sideq.append((y, x))
                # do something
            if self.garden_map[y, x] != value:
                continue

            if not(self._is_same(y,x-1, value)):
                if not(self._is_same(y-1,x, value)):
                    sides += 1 # top edge
                if not(self._is_same(y+1,x, value)):
                    sides += 1 # bottom edge
            else:
                if self._is_same(y-1, x-1, value) and y-1 >= 0 and not(self._is_same(y-1, x, value)):
                    sides += 1 # top edge L corner
                if self._is_same(y+1, x-1, value) and y+1 < self.garden_map.shape[0] and not(self._is_same(y+1, x, value)):
                    sides += 1 # top edge ⌜ corner
            if not(self._is_same(y-1,x, value)):
                if not(self._is_same(y,x-1, value)):
                    sides += 1 # left edge
                if not(self._is_same(y,x+1, value)):
                    sides += 1 # right edge
            else:
                if self._is_same(y-1, x-1, value) and x-1 >= 0 and not(self._is_same(y, x-1, value)):
                    sides += 1 # left edge ⌝ corner 
                if self._is_same(y-1, x+1, value) and x+1 < self.garden_map.shape[1] and not(self._is_same(y, x+1, value)):
                    sides += 1 # left edge ⌜ corner

            group_size += 1
            for d in directions:
                new_x = x + d[0]
                new_y = y + d[1]
                if new_x < 0 or new_x >= self.garden_map.shape[1] or new_y < 0 or new_y >= self.garden_map.shape[0]:
                    group_perimiter += 1
                    continue
                if 0 <= new_x < self.garden_map.shape[1] and 0 <= new_y < self.garden_map.shape[0] and \
                   not(self.visit_map[new_y, new_x]) and self.garden_map[new_y, new_x] == value:
                    q.append((new_y, new_x))
                if self.garden_map[new_y, new_x] != value:
                    group_perimiter += 1
        return (group_size, group_perimiter, group_perimiter*group_size, sides)
    
    def find_groups(self) -> int:
        groups:List[GardenGroup] = []
        for y in range(self.garden_map.shape[0]):
            for x in range(self.garden_map.shape[1]):
                if not self.visit_map[y, x]:
                    groups.append(self.visit_group(y, x, self.garden_map[y, x]))
        # print(groups)
        return sum([group[2] for group in groups])
    
    def find_groups_2(self) -> int:
        groups:List[GardenGroup] = []
        for y in range(self.garden_map.shape[0]):
            for x in range(self.garden_map.shape[1]):
                if not self.visit_map[y, x]:
                    groups.append(self.visit_group(y, x, self.garden_map[y, x]))
        # print(groups)
        return sum([(group[0] * group[3]) for group in groups])
        
def main(fn: str):
    with open(fn) as f:
        s = Solution()
        data = f.read().strip()
        s.load(data)
        t1 = time.time()
        print(s.find_groups())
        t2 = time.time()
        print(f"find_groups {t2-t1:.4f} seconds")
        s.load(data)
        t1 = time.time()
        print(s.find_groups_2())
        t2 = time.time()
        print(f"find_groups_2 {t2-t1:.4f} seconds")

if __name__ == "__main__":
    main("input.txt")
