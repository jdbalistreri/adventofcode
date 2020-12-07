from shared.io import *

DAY = "day01"
TEST_INPUT_FILE = f"/y2019/input/{DAY}_test.txt"
INPUT_FILE = f"/y2019/input/{DAY}.txt"

def get_fuel(mass):
    return mass // 3 - 2

def get_total_fuel(mass):
    total_fuel = 0
    next_fuel = get_fuel(mass)
    while next_fuel  > 0:
        total_fuel += next_fuel
        next_fuel = get_fuel(next_fuel)

    return total_fuel

def part_one(values):
    return sum([get_fuel(int(mass)) for mass in values])

def part_two(values):
    return sum([get_total_fuel(int(mass)) for mass in values])

def main():
    # test_values = read_input(TEST_INPUT_FILE)
    values = read_input(INPUT_FILE)
    # print(part_one(test_values))
    print(part_one(values))
    # print(part_two(test_values))
    print(part_two(values))
