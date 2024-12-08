import math, string
import re, os
import numpy as np
from pprint import pprint
import functools, itertools

def part1(lines):
    lines = np.array([list(x) for x in lines])
    variations = list()
    for _ in range(4):
        lines = np.rot90(lines)
        variations.append("".join(lines.flatten()))
    for i in range(len(lines)//2):
        if i == 0:
            diag = np.diagonal(lines, offset=i)
        else:
            diag = np.diagonal(lines, offset=i) + np.diagonal(lines, offset=-i)
    print(len(variations))
    return

def part2(lines):
    return

if __name__ == "__main__":
    filename = os.path.basename(__file__)
    dayNumber = re.sub(r"^.*?(\d+)\.py$", r"\1", filename)
    yearNumber = os.path.basename(os.path.dirname(os.path.dirname(__file__)))

    inputFile = os.path.join(
            os.path.dirname(__file__),
            '../input-files/',
            f'adventofcode.com_{yearNumber}_day_{dayNumber}_input.txt'
            )
    inputFile = os.path.normpath(inputFile)

    with open(inputFile, 'r') as f:
        lines = f.readlines()
        lines = list(map(str.strip, lines))

    print(part1(lines))
    print(part2(lines))