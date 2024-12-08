from typing import List, Tuple, Dict, Set
from collections import defaultdict

MapList = List[str]
AntennaDict = Dict[str, List[Tuple[int, int]]]
AntinodeList = Set[Tuple[int, int]]

class Solution:
    def __init__(self):
        self.map: MapList = []
        self.antennas: AntennaDict = defaultdict(list)
        self.antinodes: AntinodeList = set()
        self.resonant_antinodes: AntinodeList = set()
    
    def load_map(self, input: str) -> Tuple[int, int]:
        self.map = input.splitlines()
        self.map_height = len(self.map)
        self.map_width = len(self.map[0])

        assert all(len(x) == len(self.map[0]) for x in self.map), "Not all elements in the array have the same value"

        self.find_antennas()
        self.find_antinodes()
        self.find_resonant_antinodes()

        return self.map_height, self.map_width

    def find_antennas(self):
        for y, row in enumerate(self.map):
            for x, cell in enumerate(row):
                if cell != '#' and cell != '.':
                    self.antennas[cell].append((y, x))

    def find_antinodes(self):
        for _, locations in self.antennas.items():
            for i in range(len(locations)):
                node1 = locations[i]
                for j in range(i+1, len(locations)):
                    node2 = locations[j]
                    y_diff = node2[0] - node1[0]
                    x_diff = node2[1] - node1[1]
                        
                    antenna1 = (node1[0] - y_diff, node1[1] - x_diff)
                    antenna2 = (node2[0] + y_diff, node2[1] + x_diff)
                    if 0 <= antenna1[0] < self.map_height and 0 <= antenna1[1] < self.map_width:
                        self.antinodes.add(antenna1)
                    if 0 <= antenna2[0] < self.map_height and 0 <= antenna2[1] < self.map_width:
                        self.antinodes.add(antenna2)

    def find_resonant_antinodes(self):
        for _, locations in self.antennas.items():
            for i in range(len(locations)):
                node1 = locations[i]
                for j in range(i+1, len(locations)):
                    node2 = locations[j]
                    y_diff = node2[0] - node1[0]
                    x_diff = node2[1] - node1[1]

                    mult_factor = 0
                    while True:
                        antenna1 = (node1[0] - y_diff*mult_factor, node1[1] - x_diff*mult_factor)
                        if 0 <= antenna1[0] < self.map_height and 0 <= antenna1[1] < self.map_width:
                            self.resonant_antinodes.add(antenna1)
                        else:
                            break
                        mult_factor += 1

                    mult_factor = 0
                    while True:
                        antenna2 = (node2[0] + y_diff*mult_factor, node2[1] + x_diff*mult_factor)
                        if 0 <= antenna2[0] < self.map_height and 0 <= antenna2[1] < self.map_width:
                            self.resonant_antinodes.add(antenna2)
                        else:
                            break
                        mult_factor += 1

    def print_map(self):
        map2 = [list(x) for x in self.map]
        for y, x in self.antinodes:
            map2[y][x] = '#'
        for l in map2:
            print(''.join(l))


def main(fn: str):
    with open(fn) as f:
        s = Solution()
        data = f.read()
        s.load_map(data)
        # for key in s.antennas.keys():
        #     data2 = list(data)
        #     for i in range(len(data2)):
        #         if data2[i] not in ['.', '\n', key]:
        #             data2[i] = '.'
        #     data2 = ''.join(data2)
        #     print(data2)
        #     print()
        #     s2 = Solution()
        #     s2.load_map(data2)
        #     print([x for x in s2.antinodes])
        #     s2.print_map()
        #     print()

        print(len(s.antinodes))
        print(len(s.resonant_antinodes))

if __name__ == "__main__":
    main("input.txt")

# submissions
# 250 - too high