from shared.io import *
import sys

DAY = "day03"
TEST_INPUT_FILE = f"/y2019/input/{DAY}_test.txt"
INPUT_FILE = f"/y2019/input/{DAY}.txt"


def moves_to_pairs(moves):
    pairs = []
    prev = (0,0)
    for move in moves.split(","):
        dir = move[0]
        x, y = prev
        delta = int(move[1:])
        if dir == "R":
            x = x + delta
        elif dir == "U":
            y = y + delta
        elif dir == "D":
            y = y - delta
        elif dir == "L":
            x = x - delta
        next = (x, y)
        pair = (prev, next)
        pairs.append(pair)
        prev = next
    return pairs

def pair_contains(pair, point):
    xp, yp = point
    start, end = pair
    x1, y1 = start
    x2, y2 = end
    return min(x1, x2) <= xp <= max(x1, x2) and min(y1, y2) <= yp <= max(y1, y2)

def contains(wire, point):
    for pair in wire:
        if pair_contains(pair, point):
            return True
    return False

def intersections(wire1, wire2):
    intersections = []
    for pair in wire1:
        start, end = pair
        x1, y1 = start
        x2, y2 = end
        for xt in range(min(x1, x2), max(x1, x2)+1):
            for yt in range(min(y1, y2), max(y1, y2)+1):
                point = (xt, yt)
                if contains(wire2, point):
                    intersections.append(point)
    return intersections

def mh_distance(point):
    return abs(point[0]) + abs(point[1])

def part_one(values):
    wire_1_moves = values[0]
    wire_2_moves = values[1]
    wire1 = moves_to_pairs(wire_1_moves)
    wire2 = moves_to_pairs(wire_2_moves)
    inter = intersections(wire1, wire2)

    min_mh_distance = sys.maxsize
    best_point = (sys.maxsize, sys.maxsize)
    for i in inter:
        mh = mh_distance(i)
        if mh == 0:
            continue
        if mh < min_mh_distance:
            best_point = i
            min_mh_distance = mh

    return best_point, min_mh_distance

def distance_between(pair):
    x1, y1 = pair[0]
    x2, y2 = pair[1]
    return abs(x2 - x1) + abs(y2 - y1)

def steps_to(point, wire):
    steps = 0
    for pair in wire:
        if pair_contains(pair, point):
            steps += distance_between((pair[0], point))
            break
        steps += distance_between(pair)
    return steps

def part_two(values):
    wire_1_moves = values[0]
    wire_2_moves = values[1]
    wire1 = moves_to_pairs(wire_1_moves)
    wire2 = moves_to_pairs(wire_2_moves)
    inter = intersections(wire1, wire2)

    min_steps = sys.maxsize
    best_point = (sys.maxsize, sys.maxsize)
    for point in inter[1:]:
        steps = steps_to(point, wire1) + steps_to(point, wire2)
        if steps < min_steps:
            best_point = point
            min_steps = steps
    return min_steps


def main():
    test_values = read_input(TEST_INPUT_FILE)
    values = read_input(INPUT_FILE)
    print(part_one(test_values))
    print(part_one(values))
    print(part_two(test_values))
    print(part_two(values))
