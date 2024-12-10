from typing import List, Iterable, Tuple
import numpy as np
import numpy.typing as npt

TrailmapArray = npt.NDArray[np.int8]

class Solution:
    def __init__(self):
        self.trailmap: TrailmapArray = np.array([])

    def load_trailmap(self, input: Iterable[str]) -> TrailmapArray:
        lines = [x.strip() for x in input if x.strip()]
        self.trailmap = np.array([[-1 if x == '.' else int(x) for x in line] for line in lines], 
                                 dtype=np.int8)
        return self.trailmap

    def trailmap_to_string(self) -> str:
        return '\n'.join(''.join('.' if x < 0 else str(x) for x in row) for row in self.trailmap)
    
    def find_trails(self)->List[List[Tuple[int, int]]]:
        zero_positions: List[Tuple[int, int]] = list((int(x), int(y)) for x,y in zip(*np.where(self.trailmap==0)))
        trails = [self.find_trails_from_point(x) for x in zero_positions]
        return trails

    def _find_trails_recursive(self, pos: Tuple[int, int], value: int, visit_map: TrailmapArray) -> List[Tuple[int, int]]:
        rv: List[Tuple[int, int]] = []
        if visit_map[pos] == 1:
            return []
        visit_map[pos] = 1
        if value == 9:
            return [pos]
        # check the points in the four cardinal directions around pos
        # if the value is 1 more than the current value, recurse

        for point in [(pos[0]+1, pos[1]), (pos[0]-1, pos[1]), (pos[0], pos[1]+1), (pos[0], pos[1]-1)]:
            if 0 <= point[0] < self.trailmap.shape[0] and 0 <= point[1] < self.trailmap.shape[1]:
                if self.trailmap[point] == value + 1:
                    rv = rv + self._find_trails_recursive(point, value + 1, visit_map)
        return rv

    def find_trails_from_point(self, start: Tuple[int, int]) -> List[Tuple[int, int]]:
        visit_map = np.zeros(self.trailmap.shape, dtype=np.int8)
        trails = self._find_trails_recursive(start, self.trailmap[start], visit_map)
        return trails

    def find_all_trails(self)->List[List[Tuple[int, int]]]:
        zero_positions: List[Tuple[int, int]] = list((int(x), int(y)) for x,y in zip(*np.where(self.trailmap==0)))
        trails = [self.find_all_trails_from_point(x) for x in zero_positions]
        return trails

    def _find_all_trails_recursive(self, pos: Tuple[int, int], value: int) -> List[Tuple[int, int]]:
        rv: List[Tuple[int, int]] = []
        if value == 9:
            return [pos]
        # check the points in the four cardinal directions around pos
        # if the value is 1 more than the current value, recurse

        for point in [(pos[0]+1, pos[1]), (pos[0]-1, pos[1]), (pos[0], pos[1]+1), (pos[0], pos[1]-1)]:
            if 0 <= point[0] < self.trailmap.shape[0] and 0 <= point[1] < self.trailmap.shape[1]:
                if self.trailmap[point] == value + 1:
                    rv = rv + self._find_all_trails_recursive(point, value + 1)
        return rv

    def find_all_trails_from_point(self, start: Tuple[int, int]) -> List[Tuple[int, int]]:
        trails = self._find_all_trails_recursive(start, self.trailmap[start])
        return trails

def main(fn: str):
    with open(fn) as f:
        s = Solution()
        data = f.readlines()
        s.load_trailmap(data)
        trails = s.find_trails()
        print(sum(len(x) for x in trails))
        all_trails = s.find_all_trails()
        print(sum(len(x) for x in all_trails))

if __name__ == "__main__":
    main("input.txt")
