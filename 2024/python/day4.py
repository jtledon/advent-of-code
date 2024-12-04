import math, string
import re, os
# import numpy as np
from pprint import pprint

def part1(lines):
    matrix = map(list, lines)
    print(list(matrix))
    # left to right
    # right to left
    # top to bottom
    # bottom to top
    # top right to bottom left
    # bottom left to top right
    # top left to bottom right
    # bottom right to top left
    # align them all into one long string and then just use a re.findall() and count ocurrences

    # top and left starting indicies

    # or just this lol np.diagonal(matrix, offset=1)
    topAndLeftStart = [(0, col) for col in len(matrix)] + []
    # combine all of the diagonals
    # reverse the string to get the
    return

def part2(lines):
    return

if __name__ == "__main__":
    filename = os.path.basename(__file__)
    dayNumber = re.sub(r"^.*(\d+)\.py$", r"\1", filename)
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
