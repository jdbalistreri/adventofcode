import os

def read_input(filename):
    with open(os.getcwd() + filename, "r") as f:
        content = f.readlines()
    return [x.strip() for x in content]

SUM_TARGET = 2020

def get_two_entries(values_set, sum_target=SUM_TARGET):
    for value in values_set:
        complement = sum_target - value
        if complement in values_set:
            return value, complement, complement*value
    return None, None, None

def get_three_entries(values_set):
    for v1 in values_set:
        sub_target = SUM_TARGET - v1
        value, complement, product = get_two_entries(values_set, sub_target)
        if value != None:
            return value, complement, v1, value*complement*v1
    return None, None, None, None

def main():
    values = set([int(x) for x in  read_input("/input/01.txt")])
    print(get_two_entries(values))
    print(get_three_entries(values))


if __name__ == "__main__":
    main()
