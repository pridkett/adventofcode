from typing import List, TypeAlias, TypedDict, Tuple
import numpy as np
import numpy.typing as npt
import re
import math

RobotLocationArray:TypeAlias = npt.NDArray[np.int8]

class RobotType(TypedDict):
    pos: Tuple[int, int]
    vel: Tuple[int, int]

class Solution:
    def __init__(self):
        self.dimensions: Tuple[int, int] = (-1, -1)
        self.robots:List[RobotType] = []
        self.parse_regex = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")

    def set_dimensions(self, dimensions: Tuple[int, int]):
        self.dimensions = dimensions

    def load_robots(self, input:str):
        for line in [x.strip() for x in input.splitlines() if x.strip() != ""]:
            m = self.parse_regex.match(line)
            if m:
                self.robots.append({'pos': (int(m.group(1)), int(m.group(2))), 'vel': (int(m.group(3)), int(m.group(4)))})
            else:
                print(f"Invalid line: [{line}]")

    def _robots_to_ndarray(self) -> RobotLocationArray:
        robot_map = np.zeros(self.dimensions, dtype=np.int8)
        for robot in self.robots:
            robot_map[robot['pos'][0], robot['pos'][1]] += 1
        return robot_map
    
    def get_map(self) -> str:
        robot_map = self._robots_to_ndarray()
        map = "\n".join(["".join([str(x) for x in row]) for row in robot_map.T]).replace("0", ".")
        return map

    def get_safety_factor(self) -> int:
        robot_map = self._robots_to_ndarray()
        x_splits = (0, self.dimensions[0]//2, self.dimensions[0])
        y_splits = (0, self.dimensions[1]//2, self.dimensions[1])
        quads = (((0,0), (x_splits[1],y_splits[1])), 
                 ((x_splits[1]+1, 0), (x_splits[2], y_splits[1])),
                 ((0, y_splits[1]+1), (x_splits[1], y_splits[2])),
                 ((x_splits[1]+1, y_splits[1]+1), (x_splits[2], y_splits[2])))
        return math.prod([int(np.sum(robot_map[quad[0][0]:quad[1][0], quad[0][1]:quad[1][1]])) for quad in quads])

    def tick(self, count:int):
        for i, robot in enumerate(self.robots):
            self.robots[i]['pos'] = ((robot['pos'][0] + robot['vel'][0] * count) % self.dimensions[0], (robot['pos'][1] + robot['vel'][1] * count) % self.dimensions[1])

    def get_xy_variance(self) -> Tuple[int, int]:
        x = [robot['pos'][0] for robot in self.robots]
        y = [robot['pos'][1] for robot in self.robots]
        return int(np.var(x)), int(np.var(y))

def main(fn: str):
    with open(fn) as f:
        s = Solution()
        data = f.read()
        s.set_dimensions((101, 103))
        s.load_robots(data)
        print(s.get_map())
        ctr = 0
        total_var = 99999999
        while True:
            x_var, y_var = s.get_xy_variance()
            if x_var + y_var < total_var:
                total_var = x_var + y_var
                print("*"*80)
                print(f"ctr: {ctr}")
                print(s.get_map())
            s.tick(1)
            ctr = ctr + 1

if __name__ == "__main__":
    main("input.txt")


