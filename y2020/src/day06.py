from shared.io import *

INPUT_FILE = "/y2020/input/06.txt"

def part_one(values):
    groups = get_groups(values)
    return sum([len(set([y for y in x])) for x in groups])

def part_two(values):
    groups = get_groups(values, sep=',')
    count = 0
    for group in groups:
        people = group.split(",")
        total = set([y for y in people[0]])
        for remaining in people[1:]:
            next = set([y for y in remaining])
            total = total.intersection(next)
        count += len(total)
    return count

def main():
    values = read_input(INPUT_FILE)
    print(part_one(values))
    print(part_two(values))
