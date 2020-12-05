import re

from shared.io import *

INPUT_FILE = "/y2020/input/03.txt"
TREE_SYMBOL = "#"

def trees_for_slope(values, right, down):
    x = 0
    y = 0
    count = 0
    while y < len(values):
        if values[y][x] == TREE_SYMBOL:
            count += 1
        x = (x + right) % len(values[y])
        y += down
    return count

def main():
    values = read_input(INPUT_FILE)
    print(trees_for_slope(values, 3, 1))
    print(
        trees_for_slope(values, 1, 1) *
        trees_for_slope(values, 3, 1) *
        trees_for_slope(values, 5, 1) *
        trees_for_slope(values, 7, 1) *
        trees_for_slope(values, 1, 2)
    )
