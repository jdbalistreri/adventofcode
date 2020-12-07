import re

from shared.io import *

INPUT_FILE = "/y2020/input/05.txt"

def to_int(s):
    return int(s.replace("F", "0").replace("B", "1"), 2)

def to_int_2(s):
    return int(s.replace("L", "0").replace("R", "1"), 2)

def from_hash(s):
    row = to_int(s[:7])
    col = to_int_2(s[7:])
    seat = row * 8 + col
    return seat

def main():
    values = read_input(INPUT_FILE)
    seats = [from_hash(x) for x in values]
    seats.sort()
    i = 0
    while i <= len(seats):
        if seats[i] + 2 == seats[i+1]:
            print(seats[i] + 1)
            break
        i += 1
