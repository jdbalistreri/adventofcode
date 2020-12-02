import re

from shared.io import *

INPUT_FILE = "/y2020/input/02.txt"
REGEX = re.compile("^(\d+)-(\d+) (\w): (\w+)$")


def apply_policy(values, policy_fn):
    total_valid = 0
    for value in values:
        pieces = REGEX.findall(value)[0]
        p0, p1, expected_char, password = int(pieces[0]), int(pieces[1]), pieces[2], pieces[3]
        if policy_fn(password, p0, p1, expected_char):
            total_valid += 1
    print(total_valid)

def policy_one(pw, p0, p1, char):
    count = 0
    for c in pw:
        if c == char:
            count += 1
    return count <= p1 and count >= p0

def policy_two(pw, p0, p1, char):
    char1 = pw[p0-1]
    char2 = pw[p1-1]
    return ((char1 == char) or (char2 == char)) and (char1 != char2)

def main():
    values = read_input(INPUT_FILE)
    apply_policy(values, policy_one)
    apply_policy(values, policy_two)
