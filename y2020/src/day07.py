import re

from shared.io import *

DAY = "07"
TEST_INPUT_FILE = f"/y2020/input/{DAY}_test.txt"
INPUT_FILE = f"/y2020/input/{DAY}.txt"

pass_one_regex = re.compile(r"^(.+) bags contain (.*)\.$")
pass_two_regex = re.compile(r"(\d+) ([\w\s]+) bag[s]?")

def parse_bags(values):
    bags_to_contents = {}
    for value in values:
        found = pass_one_regex.findall(value)[0]
        contents = {x[1]: int(x[0]) for x in pass_two_regex.findall(found[1])}
        bags_to_contents[found[0]] = contents
    return bags_to_contents

starting_bag = 'shiny gold'

def part_one(values):
    containing_to_contained = parse_bags(values)

    contained_to_containing = {}

    for containing, contained in containing_to_contained.items():
        for contained_bag in contained.keys():
            containing_bags = contained_to_containing.get(contained_bag, [])
            containing_bags.append(containing)
            contained_to_containing[contained_bag] = containing_bags

    seen_bags = set()
    queue = contained_to_containing[starting_bag]
    while queue:
        next_bag = queue.pop()
        seen_bags.add(next_bag)
        bags_to_append = contained_to_containing.get(next_bag, [])
        for bag_to_append in bags_to_append:
            if bag_to_append not in seen_bags:
                queue.append(bag_to_append)

    return len(seen_bags)


def part_two(values):
    containing_to_contained = parse_bags(values)

    def num_bags_contained(bag, memo):
        if bag in memo:
            return memo[bag]

        contained = containing_to_contained.get(bag, {})
        if len(contained) == 0:
            return 0

        total = 0
        for inner_bag, count in contained.items():
            total += (num_bags_contained(inner_bag, memo) + 1) * count

        memo[bag] = total
        return memo[bag]

    outer_memo = {}
    return num_bags_contained(starting_bag, outer_memo)

def main():
    test_values = read_input(TEST_INPUT_FILE)
    values = read_input(INPUT_FILE)
    print(part_one(test_values))
    print(part_one(values))
    print(part_two(test_values))
    print(part_two(values))
