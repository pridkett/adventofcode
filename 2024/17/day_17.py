from typing import List, TypeAlias, TypedDict, Tuple, Dict, Set
import numpy as np
import numpy.typing as npt
from collections import defaultdict, deque
from dataclasses import dataclass, field

from rich.live import Live
from rich.table import Table
import termios, sys, tty


INST_MAP = { 0: 'adv', 1: 'bxl', 2: 'bst', 3: 'jnz', 4: 'bxc', 5: 'out', 6: 'bdv', 7: 'cdv'}
INV_INST_MAP = {v: k for k, v in INST_MAP.items()}
ProgramOutput:TypeAlias = List[int]

class RegisterDict(TypedDict):
    A: int
    B: int
    C: int

class Solution:
    def __init__(self):
        self._registers:RegisterDict = {'A': 0, 'B': 0, 'C': 0}
        self.pc = 0

        self.program:List[int]

    @property
    def registers(self) -> RegisterDict:
        return self._registers
    
    def load(self, input:str):
        for line in input.splitlines():
            if line.startswith("Register"):
                parts = line.split()
                self._registers[parts[1][0]] = int(parts[2])
            elif line.startswith("Program"):
                self.program = [int(x) for x in line.split(':')[1].strip().split(',')]
    
    def generate_table(self, output: List[int]) -> Table:
        program_table = Table()
        program_table.add_column("PC", style="bold yellow")
        program_table.add_column("Address")
        program_table.add_column("Instruction")
        program_table.add_column("Operand")
        ctr = 0
        while ctr < len(self.program):
            inst = self.program[ctr]
            operand = self.program[ctr + 1]
            pcmarker = ""
            if self.pc == ctr:
                pcmarker = ">>>"
            program_table.add_row(pcmarker, str(ctr), INST_MAP[inst], str(operand))
            ctr = ctr + 2

        register_table = Table()
        register_table.add_column("Register")
        register_table.add_column("Value", width=15)
        for k, v in self.registers.items():
            register_table.add_row(k, str(v))

        output_table = Table(expand=True)
        output_table.add_column("Output")
        output_table.add_row(",".join([str(x) for x in output]))

        subtable = Table.grid()
        subtable.add_row(program_table, register_table)
        combined_table = Table.grid()
        combined_table.add_row(subtable)
        combined_table.add_row(output_table)

        return combined_table

    def print_program_status(self):
        pass

    def run_with_output(self)-> str:
        output:ProgramOutput = []
        with Live(self.generate_table(output)) as live:
    
            while self.pc < len(self.program):
                live.update(self.generate_table(output))

                inst = self.program[self.pc]
                operand = self.program[self.pc + 1]

                output.extend(self.__getattribute__(f"op_{INST_MAP[inst]}")(operand))

                self.pc = self.pc + 2
                tty.setcbreak(sys.stdin)
                sys.stdin.read(1)

        return ",".join([str(x) for x in output])
    
    def run(self)-> ProgramOutput:
        output:ProgramOutput = []
        while self.pc < len(self.program):
            inst = self.program[self.pc]
            operand = self.program[self.pc + 1]

            output.extend(self.__getattribute__(f"op_{INST_MAP[inst]}")(operand))

            self.pc = self.pc + 2
        return output
    
    def _get_combo_operand(self, operand:int) -> int:
        if 0 <= operand <= 3:
            return operand
        if operand == 4:
            return self.registers['A']
        if operand == 5:
            return self.registers['B']
        if operand == 6:
            return self.registers['C']
        assert(f"Invalid operand: pc={self.pc}, operand={operand}")
        return 0

    def op_adv(self, operand:int) -> ProgramOutput:
        op = self._get_combo_operand(operand)
        self.registers['A'] = self.registers['A'] // (2**op)
        return []

    def op_bxl(self, operand:int) -> ProgramOutput:        
        self.registers['B'] = self.registers['B'] ^ operand
        return []

    def op_bst(self, operand:int) -> ProgramOutput:
        self.registers['B'] = self._get_combo_operand(operand) % 8
        return []
    
    def op_jnz(self, operand:int) -> ProgramOutput:
        if self.registers['A'] == 0:
            return []
        self.pc = operand -2
        return []
    
    def op_bxc(self, operand:int) -> ProgramOutput:
        self.registers['B'] = self.registers['B'] ^ self.registers['C']
        return []

    def op_out(self, operand:int) -> ProgramOutput:
        op = self._get_combo_operand(operand)
        return [op % 8]

    def op_bdv(self, operand:int) -> ProgramOutput:
        op = self._get_combo_operand(operand)
        self.registers['B'] = self.registers['A'] // (2**op)
        return []

    def op_cdv(self, operand:int) -> ProgramOutput:
        op = self._get_combo_operand(operand)
        self.registers['C'] = self.registers['A'] // (2**op)
        return []
        
    def reverse_calc(self, target_output:List[int]):
        pos_ctr = len(target_output) - 1
        a = 8 ** (len(target_output) - 1)
        while True:
            self.pc = 0
            self.registers['A'] = a
            output = self.run()
            if pos_ctr <= -1:
                break
            if output[pos_ctr] == target_output[pos_ctr]:
                pos_ctr = pos_ctr - 1
                continue
            a = a + 8**pos_ctr
            if a > 8**16 or pos_ctr == -1:
                break
        return a

def main(fn: str):
    with open(fn) as f:
        s = Solution()
        data = f.read()
        s.load(data)
        # print(s.run_with_output())
        print(",".join([str(x) for x in s.run()]))
        print(s.reverse_calc(s.program))

if __name__ == "__main__":
    main("input.txt")


