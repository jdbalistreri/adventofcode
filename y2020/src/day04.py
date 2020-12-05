import re

from shared.io import *

INPUT_FILE = "/y2020/input/04.txt"

def clean_values(values):
    curr_passport = ""
    passports = []
    for value in values:
        if value == "":
            passports.append(curr_passport.strip())
            curr_passport = ""
        else:
            curr_passport += " " + value

    if curr_passport != "":
        passports.append(curr_passport.strip())

    return passports

KEYS_WE_WANT = set(["byr", "ecl", "eyr", "hcl", "hgt", "iyr", "pid"])

def is_valid_year(year, start, end):
    return len(year) == 4 and year >= start and year <= end

def is_valid_height(height):
    if len(height) < 2:
        return False
    suffix = height[-2:]
    rest = height[:-2]
    if suffix == "cm":
        return rest >= "150" and rest <= "193"
    elif suffix == "in":
        return rest >= "59" and rest <= "76"
    return False

eye_color_regex = re.compile("^#[0-9a-f]{6}$")
pid_regex = re.compile("^[0-9]{9}$")
ecl_set = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])

def is_valid(passport):
    values = {x.split(":")[0] : x.split(":")[1].strip() for x in passport.split(" ")}
    if not len(set(values.keys()).intersection(KEYS_WE_WANT)) == 7:
        return str(set(values.keys()))

    if not is_valid_year(values["byr"], "1920", "2002"):
        return "byr:" + values["byr"]

    if not is_valid_year(values["iyr"], "2010", "2020"):
        return "iyr:" + values["iyr"]

    if not is_valid_year(values["eyr"], "2020", "2030"):
        return "eyr:" + values["eyr"]

    if not is_valid_height(values["hgt"]):
        return "hgt:" + values["hgt"]

    if eye_color_regex.match(values["hcl"]) is None:
        return "hcl:" + values["hcl"]

    if values["ecl"] not in ecl_set:
        return "ecl:" + values["ecl"]

    if pid_regex.match(values["pid"]) is None:
        return "pid:" + values["pid"]

    return None


def main():
    values = read_input(INPUT_FILE)
    passports = clean_values(values)
    count = 0
    invalids = []
    for passport in passports:
        result = is_valid(passport)
        if result is None:
            count += 1
        else:
            invalids.append(result)
    invalids.sort()
    [print(x) for x in invalids]
    print(count)
