from shared.io import *

DAY = "day02"
TEST_INPUT_FILE = f"/y2019/input/{DAY}_test.txt"
INPUT_FILE = f"/y2019/input/{DAY}.txt"

def run(program):
    i = 0
    while i < len(program):
        op = program[i]
        if op == 1:
            pos1 = program[i+1]
            pos2 = program[i+2]
            pos3 = program[i+3]
            sum = program[pos1] + program[pos2]
            program[pos3] = sum
        elif op == 2:
            pos1 = program[i+1]
            pos2 = program[i+2]
            pos3 = program[i+3]
            product = program[pos1] * program[pos2]
            program[pos3] = product
        elif op == 99:
            break
        else:
            raise ValueError(f"unknown op {op}")

        i += 4

def part_one(values):
    for value in values:
        program = [int(x) for x in value.split(",")]
        run(program)
        print(program)


def part_two(values):
    initial_memory = [int(x) for x in values[0].split(",")]

    for noun in range(0,100):
        for verb in range(0, 100):
            test_memory = initial_memory.copy()
            test_memory[1] = noun
            test_memory[2] = verb
            run(test_memory)
            result = test_memory[0]
            if result == 19690720:
                print(f"answer: {noun*100 + verb}")
                return

def main():
    test_values = read_input(TEST_INPUT_FILE)
    values = read_input(INPUT_FILE)
    print(part_one(test_values))
    print(part_one(values))
    # print(part_two(test_values))
    part_two(values)
