from typing import List, TypeAlias, TypedDict, Tuple, Dict, Set
import numpy as np
import numpy.typing as npt
from collections import defaultdict

BlockMap:TypeAlias = Dict[int, Set[int]]
MapType:TypeAlias = npt.NDArray[np.int8]
REPLACEMENT_MAPPING:Dict[str, str] = {'.': '..', '#': '##', 'O': '[]', '@': '@.'}
CHAR_MAPPING:Dict[int, str] = {0: '.', -1: '#', 1: 'O', 2: '@', 3: '[', 4: ']'}
INV_CHAR_MAPPING:Dict[str, int] = {v: k for k, v in CHAR_MAPPING.items()}

class RobotType(TypedDict):
    pos: Tuple[int, int]
    vel: Tuple[int, int]

class Solution:
    def __init__(self):
        self._map: MapType = np.zeros((0,0), dtype=np.int8)
        self._instructions: str = ''
        self.dimensions: Tuple[int, int] = (-1, -1)
        self.robot_pos: List[int] = [-1, -1]
        self.inst_ptr = 0
        self.advanced_map = False

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
        # for row in self._map:
        #     this_row = "".join([self.get_char(x) for x in row])
        #     print(this_row)
        return "\n".join(["".join([self.get_char(x) for x in row]) for row in self._map])

    @map.setter
    def map(self, map_str: str):
        self._map = np.array([[self.translate_char(x) for x in line.strip()] for line in map_str.splitlines()], dtype=np.int8)
        self.dimensions = self._map.shape

        robot_positions = np.argwhere(self._map == 2)
        if robot_positions.size > 0:
            self.robot_pos = list(robot_positions[0])
        else:
            assert("No robot found in map")

    def set_advanced_map(self, map_str: str):
        new_map:List[str] = []
        for x in map_str:
            if x in REPLACEMENT_MAPPING:
                new_map.append(REPLACEMENT_MAPPING[x])
            else:
                new_map.append(x)
        self.map = "".join(new_map)
        self.advanced_map = True

    @property
    def instructions(self) -> str:
        return self._instructions

    @instructions.setter
    def instructions(self, instructions: str):
        self._instructions = ''.join([x.strip() for x in instructions])

    def load(self, input:str, advanced:bool=False):
        map_str = ""
        instructions_str = ""
        for line in input.splitlines():
            if line == "":
                continue
            if line[0] == '#':
                map_str = map_str + line + "\n"
            else:
                instructions_str = instructions_str + line

        if not(advanced):
            self.map = map_str
        else:
            self.set_advanced_map(map_str)
        self.instructions = instructions_str

    def run(self):
        # print(self.map)
        # print(f"tick: {self.inst_ptr} - {self.instructions[self.inst_ptr]}")
        while self.tick():
            # print(self.map)
            # if len(self.instructions) > self.inst_ptr:
            #     print(f"tick: {self.inst_ptr} - {self.instructions[self.inst_ptr]}")
            # else:
            #     print(f"final tick: {self.inst_ptr}") 
            pass
        pass

    def tick(self, steps:int=1) -> bool:
        for _ in range(steps):
            if self.inst_ptr >= len(self.instructions):
                return False
            inst = self.instructions[self.inst_ptr]
            if inst == '^':
                y,x = self.robot_pos
                if self.advanced_map:
                    blocks_to_move:BlockMap = defaultdict(set)
                    blocks_to_move[y] = set([x])
                    breakout = False
                    while True:
                        y = y - 1
                        if y < 0 or breakout:
                            break
                        if len(blocks_to_move[y+1]) == 0:
                            for row in blocks_to_move:
                                for xpos in blocks_to_move[row]:
                                    self._map[row, xpos] = INV_CHAR_MAPPING["."]
                            for row_num, row in blocks_to_move.items():
                                if len(row) % 2 == 0:
                                    elem_ctr = 0
                                    for xpos in sorted(row):
                                        if elem_ctr % 2 == 0:
                                            self._map[row_num - 1, xpos] = INV_CHAR_MAPPING["["]
                                        else:
                                            self._map[row_num - 1, xpos] = INV_CHAR_MAPPING["]"]
                                        elem_ctr = elem_ctr + 1
                                else:
                                    assert(len(row) == 1)
                                    self.robot_pos = [row_num - 1, list(row)[0]]
                                    self._map[self.robot_pos[0], self.robot_pos[1]] = INV_CHAR_MAPPING["@"]

                        for xpos in blocks_to_move[y+1]:
                            if self._map[y, xpos] == INV_CHAR_MAPPING["#"]:
                                breakout = True
                                break
                            if self._map[y, xpos] == INV_CHAR_MAPPING["["]:
                                blocks_to_move[y].add(xpos)
                                blocks_to_move[y].add(xpos+1)
                            if self._map[y, xpos] == INV_CHAR_MAPPING["]"]:
                                blocks_to_move[y].add(xpos-1)
                                blocks_to_move[y].add(xpos)

                else:
                    while True:
                        y = y - 1
                        if y < 0:
                            break
                        if self._map[y, x] == INV_CHAR_MAPPING["#"]:
                            break
                        if self._map[y, x] == INV_CHAR_MAPPING["."]:
                            for i in range(y, self.robot_pos[0]):
                                self._map[i, x] = self._map[i+1, x]
                            self._map[self.robot_pos[0], self.robot_pos[1]] = INV_CHAR_MAPPING["."]
                            self.robot_pos[0] = self.robot_pos[0] - 1
                            break
            elif inst == 'v':
                y,x = self.robot_pos
                if self.advanced_map:
                    blocks_to_move:BlockMap = defaultdict(set)
                    blocks_to_move[y] = set([x])
                    breakout = False
                    while True:
                        y = y + 1
                        if y >= self.dimensions[0] or breakout:
                            break
                        if len(blocks_to_move[y-1]) == 0:
                            for row in blocks_to_move:
                                for xpos in blocks_to_move[row]:
                                    self._map[row, xpos] = INV_CHAR_MAPPING["."]
                            for row_num, row in blocks_to_move.items():
                                if len(row) % 2 == 0:
                                    elem_ctr = 0
                                    for xpos in sorted(row):
                                        if elem_ctr % 2 == 0:
                                            self._map[row_num + 1, xpos] = INV_CHAR_MAPPING["["]
                                        else:
                                            self._map[row_num + 1, xpos] = INV_CHAR_MAPPING["]"]
                                        elem_ctr = elem_ctr + 1
                                else:
                                    assert(len(row) == 1)
                                    self.robot_pos = [row_num + 1, list(row)[0]]
                                    self._map[self.robot_pos[0], self.robot_pos[1]] = INV_CHAR_MAPPING["@"]

                        for xpos in blocks_to_move[y-1]:
                            if self._map[y, xpos] == INV_CHAR_MAPPING["#"]:
                                breakout = True
                                break
                            if self._map[y, xpos] == INV_CHAR_MAPPING["["]:
                                blocks_to_move[y].add(xpos)
                                blocks_to_move[y].add(xpos+1)
                            if self._map[y, xpos] == INV_CHAR_MAPPING["]"]:
                                blocks_to_move[y].add(xpos-1)
                                blocks_to_move[y].add(xpos)
                else:
                    while True:
                        y = y + 1
                        if y >= self.dimensions[1]:
                            break
                        if self._map[y, x] == INV_CHAR_MAPPING["#"]:
                            break
                        if self._map[y, x] == INV_CHAR_MAPPING["."]:
                            for i in range(y, self.robot_pos[0], -1):
                                self._map[i, x] = self._map[i-1, x]
                            self._map[self.robot_pos[0], self.robot_pos[1]] = INV_CHAR_MAPPING["."]
                            self.robot_pos[0] = self.robot_pos[0] + 1
                            break
            elif inst == '>':
                y,x = self.robot_pos
                while True:
                    x = x + 1
                    if x >= self.dimensions[1]:
                        break
                    if self._map[y, x] == INV_CHAR_MAPPING["#"]:
                        break
                    if self._map[y, x] == INV_CHAR_MAPPING["."]:
                        for i in range(x, self.robot_pos[1], -1):
                            self._map[y, i] = self._map[y, i-1]
                        self._map[self.robot_pos[0], self.robot_pos[1]] = INV_CHAR_MAPPING["."]
                        self.robot_pos[1] = self.robot_pos[1] + 1
                        break
            elif inst == '<':
                y,x = self.robot_pos
                while True:
                    x = x - 1
                    if x < 0:
                        break
                    if self._map[y, x] == INV_CHAR_MAPPING["#"]:
                        break
                    if self._map[y, x] == INV_CHAR_MAPPING["."]:
                        for i in range(x, self.robot_pos[1]):
                            self._map[y, i] = self._map[y, i+1]
                        self._map[self.robot_pos[0], self.robot_pos[1]] = INV_CHAR_MAPPING["."]
                        self.robot_pos[1] = self.robot_pos[1] - 1
                        break
            self.inst_ptr = self.inst_ptr + 1
            self._map[self.robot_pos[0], self.robot_pos[1]] = INV_CHAR_MAPPING["@"]
        return True

    def get_gps_score(self) -> int:
        gps_score = 0
        for y in range(self.dimensions[0]):
            for x in range(self.dimensions[1]):
                if self._map[y, x] in [INV_CHAR_MAPPING["O"], INV_CHAR_MAPPING["["]]:
                    gps_score = gps_score + (100*y +x)
        return gps_score
    
def main(fn: str):
    with open(fn) as f:
        s = Solution()
        data = f.read()
        s.load(data)
        s.run()
        print(s.get_gps_score())

        s = Solution()
        s.load(data, advanced=True)
        s.run()
        print(s.get_gps_score())


if __name__ == "__main__":
    main("input.txt")


