import os

def read_input(filename):
    with open(os.getcwd() + filename, "r") as f:
        content = f.readlines()
    return [x.strip() for x in content]
