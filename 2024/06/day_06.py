from typing import List, Sequence, Dict, Tuple, Set, Optional

GUARD_CHARS = ["^", "<", "v", ">"]

class Solution:
    def __init__(self):
        self.map: List[List[str]] = []
        self.visit_map: List[List[str]] = []
        self.map_width: int = 0
        self.map_height: int = 0

    def load_map(self, input: Sequence[str]):
        self.map = [[y for y in x.strip()] for x in input]
        self.map_width = len(self.map[0])
        self.map_height = len(self.map)

    def create_visit_map(self):
        self.visit_map = self.map.copy()

        guard_x = -1
        guard_y = -1
        guard_state = " "
        # find the guard 
        for y in range(self.map_height):
            for x in range(self.map_width):
                if self.map[y][x] in GUARD_CHARS:
                    guard_state = self.map[y][x]
                    guard_x = x
                    guard_y = y
                    self.visit_map[guard_x][guard_y] = "."
                    break
            if guard_x != -1:
                break

        while True:
            self.visit_map[guard_y][guard_x] = "X"
            # print(guard_y, guard_x, guard_state)
            if guard_state == "^":
                if guard_y == 0:
                    break
                elif self.map[guard_y-1][guard_x] == "#":
                    guard_state = ">"
                else:
                    guard_y = guard_y - 1

            elif guard_state == "v":
                if guard_y == self.map_height - 1:
                    break
                elif self.map[guard_y+1][guard_x] == "#":
                    guard_state = "<"
                else:
                    guard_y = guard_y + 1
            elif guard_state == "<":
                if guard_x == 0:
                    break
                elif self.map[guard_y][guard_x-1] == "#":
                    guard_state = "^"
                else:
                    guard_x = guard_x - 1
            elif guard_state == ">":
                if guard_x == self.map_width - 1:
                    break
                elif self.map[guard_y][guard_x+1] == "#":
                    guard_state = "v"
                else:
                    guard_x = guard_x + 1

    def place_obstacles(self):
        start_guard_x = -1
        start_guard_y = -1
        start_guard_state = " "
        # find the guard 
        for y in range(self.map_height):
            for x in range(self.map_width):
                if self.map[y][x] in GUARD_CHARS:
                    start_guard_state = self.map[y][x]
                    start_guard_x = x
                    start_guard_y = y
                    break
            if start_guard_x != -1:
                break

        self.create_visit_map()
        
        obstacle_locations:List[Tuple[int, int]] = []
        cycle_positions_ctr = 0

        for x, y in [(x, y) for x in range(self.map_width) for y in range(self.map_height)]:
            if self.visit_map[y][x] != "X":
                continue
            obstacle_visit_map: List[List[Dict[str,bool]]] = [[{} for _ in range(self.map_width)] for _ in range(self.map_height)]
            guard_x = start_guard_x
            guard_y = start_guard_y
            guard_state = start_guard_state
            while True:
                if obstacle_visit_map[guard_y][guard_x].get(guard_state, False):
                    obstacle_locations.append((x, y))
                    cycle_positions_ctr = cycle_positions_ctr + 1
                    break
                obstacle_visit_map[guard_y][guard_x][guard_state] = True
                
                if guard_state == "^":
                    if guard_y == 0:
                        break
                    elif self.map[guard_y-1][guard_x]=="#" or (guard_x, guard_y-1) == (x, y):
                        guard_state = ">"
                    else:
                        guard_y = guard_y - 1

                elif guard_state == "v":
                    if guard_y == self.map_height - 1:
                        break
                    elif self.map[guard_y+1][guard_x] == "#"  or (guard_x, guard_y+1) == (x, y):
                        guard_state = "<"
                    else:
                        guard_y = guard_y + 1
                elif guard_state == "<":
                    if guard_x == 0:
                        break
                    elif self.map[guard_y][guard_x-1] == "#"  or (guard_x-1, guard_y) == (x, y):
                        guard_state = "^"
                    else:
                        guard_x = guard_x - 1
                elif guard_state == ">":
                    if guard_x == self.map_width - 1:
                        break
                    elif self.map[guard_y][guard_x+1] == "#"  or (guard_x+1, guard_y) == (x, y):
                        guard_state = "v"
                    else:
                        guard_x = guard_x + 1

        return obstacle_locations

    def count_distinct_positions(self) -> int:
        return sum([x.count("X") for x in self.visit_map])
    
def main(fn: str):
    with open(fn) as f:
        s = Solution()
        data = f.readlines()
        s.load_map(data)
        s.create_visit_map()
        print(s.count_distinct_positions())
        s = Solution()
        s.load_map(data)
        obstacles = s.place_obstacles()
        print(len(obstacles))

if __name__ == "__main__":
    main("input.txt")
