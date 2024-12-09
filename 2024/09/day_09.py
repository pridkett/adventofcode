from typing import List, Tuple, Dict, Set
from collections import defaultdict

MapList = List[str]
AntennaDict = Dict[str, List[Tuple[int, int]]]
AntinodeList = Set[Tuple[int, int]]

class Solution:
    def __init__(self):
        self.disk_map: List[int] = []
        self.optimized_disk_map: List[int] = []
        self.unfragmented_disk_map: List[int] = []

    def load_disk_map(self, input: str):
        for i in range(len(input)):
            if i % 2 == 0:
                file_ctr = i // 2
                self.disk_map.extend([file_ctr for _ in range(int(input[i]))])
            else:
                self.disk_map.extend([-1 for _ in range(int(input[i]))])

    def optimize_disk_map(self):
        self.optimized_disk_map = self.disk_map.copy()
        end_ctr = -1
        for i in range(len(self.optimized_disk_map)):
            if self.optimized_disk_map[i] == -1:
                while self.optimized_disk_map[end_ctr] < 0:
                    end_ctr = end_ctr - 1
                    if (i + -1 * end_ctr) >= len(self.optimized_disk_map):
                        break

                self.optimized_disk_map[i] = self.optimized_disk_map[end_ctr]
                self.optimized_disk_map[end_ctr] = -2
            if self.optimized_disk_map[i] == -2:
                break

    def _scan_for_free_space(self, file_length:int, stop:int) -> int:
        free_scan_ptr = 0
        rv = - 1
        while True:
            while self.unfragmented_disk_map[free_scan_ptr] >= 0:
                free_scan_ptr = free_scan_ptr + 1
                if free_scan_ptr > stop:
                    break
                assert free_scan_ptr < len(self.unfragmented_disk_map), "Weird error scanning for free space"

            # see how long the space is
            free_scan_end_ptr = free_scan_ptr
            while self.unfragmented_disk_map[free_scan_end_ptr] < 0:
                if (free_scan_end_ptr - free_scan_ptr + 1) >= file_length:
                    rv = free_scan_ptr
                    break
                if free_scan_end_ptr > stop:
                    break
                assert free_scan_end_ptr < len(self.unfragmented_disk_map), "Weird error scanning for free space"
                free_scan_end_ptr = free_scan_end_ptr + 1

            # this fails for some reason on 4
            if rv != -1 and free_scan_end_ptr - free_scan_ptr + 1 >= file_length:
                break

            if free_scan_ptr >= stop:
                break

            free_scan_ptr = free_scan_end_ptr + 1

        return rv
    
    def unfragment_disk_map(self) -> List[int]:
        self.unfragmented_disk_map = self.disk_map.copy()
        total_length = len(self.unfragmented_disk_map)
        file_id = max(self.disk_map)

        end_ptr = -1    
        while file_id > 0:
            # scan for the location of the file from the right
            while self.unfragmented_disk_map[end_ptr] != file_id:
                end_ptr = end_ptr - 1
                assert (total_length + end_ptr) >= 0, f"file:{file_id} - Weird error scaning for end_ptr in file"

            start_ptr = end_ptr
            while self.unfragmented_disk_map[start_ptr-1] == file_id:
                start_ptr = start_ptr - 1
                assert (total_length + start_ptr) >= 0, f"file:{file_id} - Weird error scanning for start_ptr in file"

            file_length = end_ptr - start_ptr + 1            

            # scan for open locations from the left
            new_location = self._scan_for_free_space(file_length, (total_length + start_ptr))
            
            # copy the file
            if new_location != -1:
                for i in range(file_length):
                    self.unfragmented_disk_map[new_location + i] = file_id
                    self.unfragmented_disk_map[start_ptr + i] = -1
            
            file_id = file_id - 1
            end_ptr = start_ptr - 1

        return self.unfragmented_disk_map

    def unfragmented_disk_map_to_string(self) -> str:
        return ''.join('.' if x < 0 else str(x) for x in self.unfragmented_disk_map)

    def optimized_disk_map_to_string(self) -> str:
        return ''.join('.' if x < 0 else str(x) for x in self.optimized_disk_map)

    def disk_map_to_string(self) -> str:
        return ''.join('.' if x < 0 else str(x) for x in self.disk_map)

    def calculate_checksum(self) -> int:
        return sum(self.optimized_disk_map[i]*i for i in range(len(self.optimized_disk_map)) if self.optimized_disk_map[i] >= 0)

    def calculate_unfragmented_checksum(self) -> int:
        return sum(self.unfragmented_disk_map[i]*i for i in range(len(self.unfragmented_disk_map)) if self.unfragmented_disk_map[i] >= 0)

def main(fn: str):
    with open(fn) as f:
        s = Solution()
        data = f.read().strip()
        s.load_disk_map(data)
        s.optimize_disk_map()
        print(s.calculate_checksum())
        s.unfragment_disk_map()
        print(s.calculate_unfragmented_checksum())


if __name__ == "__main__":
    main("input.txt")

# submissions
# 250 - too high