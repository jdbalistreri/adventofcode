import os

def read_input(filename):
    with open(os.getcwd() + filename, "r") as f:
        content = f.readlines()
    return [x.strip() for x in content]


def get_groups(values, sep=""):
    curr_group = ""
    grouped = []
    for value in values:
        if value == "":
            grouped.append(curr_group.strip())
            curr_group = ""
        elif curr_group == "":
            curr_group += value
        else:
            curr_group += sep + value

    if curr_group != "":
        grouped.append(curr_group.strip())

    return grouped
