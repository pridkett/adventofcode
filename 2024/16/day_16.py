from typing import List, TypeAlias, TypedDict, Tuple, Dict, Set
import numpy as np
import numpy.typing as npt
from collections import defaultdict, deque
from dataclasses import dataclass, field

MapType:TypeAlias = npt.NDArray[np.int8]
CostMapType:TypeAlias = npt.NDArray[np.int32]
MapPathType:TypeAlias = List[List[Set[Tuple[int, int]]]]

CHAR_MAPPING:Dict[int, str] = {0: '.', -1: '#', 1: 'S', 2: 'E'}
INV_CHAR_MAPPING:Dict[str, int] = {v: k for k, v in CHAR_MAPPING.items()}
DIR_MAPPING:Dict[int, str] = {0: '^', 1: '>', 2: 'v', 3: '<'}
DIR_DIFF:Dict[int, Tuple[int, int]] = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
INV_DIR_MAPPING:Dict[str, int] = {v: k for k, v in DIR_MAPPING.items()}

@dataclass
class DirectionalPath:
    path: Dict[int, Set[Tuple[int, int]]] = field(default_factory=lambda: {v: set() for v in DIR_MAPPING.keys()})
    cost: Dict[int, int] = field(default_factory=lambda: {v: np.iinfo(np.int32).max for v in DIR_MAPPING.keys()})
NewMapPathType:TypeAlias = List[List[DirectionalPath]]

class Solution:
    def __init__(self):
        self._map: MapType = np.zeros((0,0), dtype=np.int8)
        self.dimensions: Tuple[int, int] = (-1, -1)
        self.robot_pos: List[int] = [-1, -1]
        self.target: List[int] = [-1, -1]
        self.robot_dir = 1

    def translate_char(self, c:str) -> int:
        if c in INV_CHAR_MAPPING:
            return INV_CHAR_MAPPING[c]
        assert(f"undefined character found: {c}")
        return 0

    def get_char(self, elem:int) -> str:
        if elem in CHAR_MAPPING:
            return CHAR_MAPPING[elem]
        assert(f"undefined character value found in map: {elem}")
        return ''
    
    @property
    def map(self) -> str:
        return "\n".join(["".join([self.get_char(x) for x in row]) for row in self._map])

    @map.setter
    def map(self, map_str: str):
        self._map = np.array([[self.translate_char(x) for x in line.strip()] for line in map_str.splitlines()], dtype=np.int8)
        self.dimensions = self._map.shape

        robot_positions = np.argwhere(self._map == INV_CHAR_MAPPING["S"])
        if robot_positions.size > 0:
            self.robot_pos = list(robot_positions[0])
        else:
            assert("No robot found in map")

        target = np.argwhere(self._map == INV_CHAR_MAPPING["E"])
        if target.size > 0:
            self.target_pos = list(target[0])
        else:
            assert("No target found in map")

    def tuple_set_to_list(self, s:set[Tuple[int, int]]) -> List[Tuple[int, int]]:
        return [(int(z[0]), int(z[1])) for z in list(s)]

    def run_orig(self) -> Tuple[int, int]:
        # create a map which is really expensive to start
        min_path_length = 0
        min_path_cost = np.iinfo(np.int32).max
        map_path:MapPathType = [[set() for _ in range(self.dimensions[1])] for _ in range(self.dimensions[0])]

        cost_map:CostMapType = np.ones(self.dimensions, dtype=np.int32) * np.iinfo(np.int32).max
        cost_map[self.robot_pos[0], self.robot_pos[1]] = 0
        q: deque[Tuple[int, int, str, int, set[Tuple[int, int]]]] = deque()
        q.append((self.robot_pos[0], self.robot_pos[1],'>', 0, set([(self.robot_pos[0], self.robot_pos[1])])))

        while q:
            y, x, direction, previous_cost, previous_path = q.popleft()
            if y == self.target_pos[0] and x == self.target_pos[1]:
                if previous_cost <= min_path_cost:
                    min_path_cost = previous_cost
                    min_path_length = len(previous_path)
                continue
            new_path = previous_path.copy()
            new_path.add((y,x))
            dir_int = INV_DIR_MAPPING[direction]
            for dir in range(4):
                turn_cost = 1000 if dir_int != dir else 0
                if dir == 0:
                    if y-1 >= 0 and self._map[y-1, x] != INV_CHAR_MAPPING["#"]:
                        if cost_map[y-1, x] >= previous_cost + 1 + turn_cost:
                            if cost_map[y-1, x] > previous_cost + 1 + turn_cost:
                                map_path[y-1][x] = new_path
                            else:
                                print(f"merging: ({y-1}, {x}) {self.tuple_set_to_list(map_path[y-1][x])} + {self.tuple_set_to_list(new_path)}")
                                map_path[y-1][x] = map_path[y-1][x].union(new_path)
                            cost_map[y-1, x] = previous_cost + 1 + turn_cost
                            q.append((y-1, x, DIR_MAPPING[0], cost_map[y-1, x], new_path))
                if dir == 1:
                    if x+1 < self.dimensions[1] and self._map[y, x+1] != INV_CHAR_MAPPING["#"]:
                        if cost_map[y, x+1] >= previous_cost + 1 + turn_cost:
                            if cost_map[y, x+1] > previous_cost + 1 + turn_cost:
                                map_path[y][x+1] = new_path
                            else:
                                print(f"merging: ({y}, {x+1}) {self.tuple_set_to_list(map_path[y][x+1])} + {self.tuple_set_to_list(new_path)}")
                                map_path[y][x+1] = map_path[y][x+1].union(new_path)                      
                            cost_map[y, x+1] = previous_cost + 1 + turn_cost
                            q.append((y, x+1, DIR_MAPPING[1], cost_map[y, x+1], new_path))
                if dir == 2:
                    if y+1 < self.dimensions[0] and self._map[y+1, x] != INV_CHAR_MAPPING["#"]:
                        if cost_map[y+1, x] >= previous_cost + 1 + turn_cost:
                            if cost_map[y+1, x] > previous_cost + 1 + turn_cost:
                                map_path[y+1][x] = new_path                        
                            else:
                                print(f"merging: ({y+1}, {x}) {self.tuple_set_to_list(map_path[y+1][x])} + {self.tuple_set_to_list(new_path)}")
                                map_path[y+1][x] = map_path[y+1][x].union(new_path)                      
                            cost_map[y+1, x] = previous_cost + 1 + turn_cost
                            q.append((y+1, x, DIR_MAPPING[2], cost_map[y+1, x], new_path))
                if dir == 3:
                    if x-1 >= 0 and self._map[y, x-1] != INV_CHAR_MAPPING["#"]:
                        if cost_map[y, x-1] >= previous_cost + 1 + turn_cost:
                            if cost_map[y, x-1] > previous_cost + 1 + turn_cost:
                                map_path[y][x-1] = new_path
                            else:
                                print(f"merging: ({y}, {x-1}) {self.tuple_set_to_list(map_path[y][x-1])} + {self.tuple_set_to_list(new_path)}")
                                map_path[y][x-1] = map_path[y][x-1].union(new_path)                      
                            cost_map[y, x-1] = previous_cost + 1 + turn_cost
                            q.append((y, x-1, DIR_MAPPING[3], cost_map[y, x-1], new_path))
        
        print(f"final path: {self.tuple_set_to_list(map_path[self.target_pos[0]][self.target_pos[1]])}")
        min_path_length = len(map_path[self.target_pos[0]][self.target_pos[1]])
        print(self.print_final_path(map_path[self.target_pos[0]][self.target_pos[1]]))
        return int(cost_map[self.target_pos[0], self.target_pos[1]]), min_path_length

    def run(self) -> Tuple[int, int]:
        # create a directional map path        
        map_path:NewMapPathType = [[DirectionalPath() for _ in range(self.dimensions[1])] for _ in range(self.dimensions[0])]

        # initialize all the starting costs to 0
        for k in DIR_MAPPING.keys():
            map_path[self.robot_pos[0]][self.robot_pos[1]].cost[k] = 0

        q: deque[Tuple[int, int, str, int, set[Tuple[int, int]]]] = deque()
        q.append((self.robot_pos[0], self.robot_pos[1],'>', 0, set([(self.robot_pos[0], self.robot_pos[1])])))

        while q:
            y, x, direction, previous_cost, previous_path = q.popleft()
            if y == self.target_pos[0] and x == self.target_pos[1]:
                map_path[y][x].path[INV_DIR_MAPPING[direction]].add((self.target_pos[0], self.target_pos[1]))
                continue
            
            new_path = previous_path.copy()
            new_path.add((y,x))
            dir_int = INV_DIR_MAPPING[direction]
            
            for dir in range(4):
                turn_cost = 1000 if dir_int != dir else 0
                new_cost = previous_cost + 1 + turn_cost
                # check map bounds
                y_mod:int = DIR_DIFF[dir][0]
                x_mod:int = DIR_DIFF[dir][1]
                if 0 <= y + y_mod < self.dimensions[0] and 0 <= x + x_mod < self.dimensions[1] and self._map[y + y_mod, x + x_mod] != INV_CHAR_MAPPING["#"]:
                    # check value of cell?
                    if map_path[y + y_mod][x + x_mod].cost[dir] >= new_cost:
                        if map_path[y + y_mod][x + x_mod].cost[dir] > new_cost:
                            map_path[y + y_mod][x + x_mod].path[dir] = new_path
                        else:
                            # print(f"merging: ({y-1}, {x}) {self.tuple_set_to_list(map_path[y-1][x])} + {self.tuple_set_to_list(new_path)}")
                            map_path[y + y_mod][x + x_mod].path[dir] = map_path[y + y_mod][x + x_mod].path[dir].union(new_path)
                        map_path[y + y_mod][x + x_mod].cost[dir] = new_cost
                        q.append((y + y_mod, x + x_mod, DIR_MAPPING[dir], new_cost, new_path))
        
        min_cost_path:int = min([map_path[int(self.target_pos[0])][int(self.target_pos[1])].cost[x] for x in DIR_MAPPING.keys()], key=int)

        final_paths: Set[Tuple[int, int]] = set()
        for k in DIR_MAPPING.keys():
            if map_path[int(self.target_pos[0])][int(self.target_pos[1])].cost[k] == min_cost_path:
                final_paths = final_paths.union(map_path[int(self.target_pos[0])][int(self.target_pos[1])].path[k])

        return min_cost_path, len(final_paths)
    
    def print_final_path(self, map_path:Set[Tuple[int, int]]) -> str:
        map2 = [[self.get_char(self._map[y, x]) for x in range(self.dimensions[1])] for y in range(self.dimensions[0])]
        for y, x in map_path:
            map2[y][x] = 'O'
        return "\n".join(["".join(row) for row in map2])
    
def main(fn: str):
    with open(fn) as f:
        s = Solution()
        data = f.read()
        s.map = data
        print(s.run())

if __name__ == "__main__":
    main("input.txt")


