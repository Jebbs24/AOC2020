from typing import NamedTuple, List


class Instruction(NamedTuple):
    operation: str
    argument: int

    @staticmethod
    def parse(line: str):
        operation, argument = line.strip().split()
        return Instruction(operation, int(argument))


class Boot:
    def __init__(self, data: List[Instruction]) -> None:
        self.instructions = data
        self.accumulator = 0
        self.index = 0
        self.exe = set()

    def run_one(self) -> None:
        operation, argument = self.instructions[self.index]
        if operation == 'acc':
            self.accumulator += argument
            self.index += 1
        elif operation == 'jmp':
            self.index += argument
        elif operation == 'nop':
            self.index += 1
        else:
            raise ValueError(f'unkown op: {operation}')

    def first_loop(self) -> None:
        executed = set()
        while self.index not in executed:
            executed.add(self.index)
            self.run_one()

    def does_terminate(self) -> bool:
        executed = set()
        while self.index not in executed:
            if self.index == len(self.instructions):
                return True
            executed.add(self.index)
            self.run_one()
        return False


def find_terminator(data: List[Instruction]) -> int:
    for i, (operation, argument) in enumerate(data):
        subbed = data[:]
        if operation == 'nop':
            subbed[i] = Instruction('jmp', argument)
        elif operation == 'jmp':
            subbed[i] = Instruction('nop', argument)
        else:
            continue

        boots = Boot(subbed)

        if boots.does_terminate():
            return boots.accumulator

    raise RuntimeError("never terminated")


with open('8.txt') as f:
    raw = f.read()

instructions = [Instruction.parse(line) for line in raw.split("\n")]
booter = Boot(instructions)
booter.first_loop()
print("Part one:", booter.accumulator)
print("Part two:", find_terminator(instructions))
