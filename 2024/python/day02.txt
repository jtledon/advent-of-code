import math, string
import re, os
# import numpy as np
from pprint import pprint

def isValid(arr):
    smallInc = all(abs(x) <= 3 for x in arr)
    sameSign = all(x < 0 for x in arr) or all(x > 0 for x in arr)
    return smallInc and sameSign

def part1(lines):
    lines = map(str.split, lines)

    diffList = list()
    for line in lines:
        line = list(map(int, line))
        lineDiff = [ line[i] - line[i+1] for i in range(len(line) - 1)]
        diffList.append(lineDiff)

    safe = 0
    for line in diffList:
        # print(line, smallInc, sameSign)
        if isValid(line):
            safe += 1

    return safe

def part2(lines):
    lines = map(str.split, lines)

    safe = 0
    for line in lines:
        line = list(map(int, line))
        lineDiff = [ line[i] - line[i+1] for i in range(len(line) - 1)]

        if isValid(lineDiff):
            safe += 1
        else:
            for i in range(len(line)):
                oneDropped = line[:i] + line[i+1:]
                lineDiff = [ oneDropped[i] - oneDropped[i+1] for i in range(len(oneDropped) - 1)]
                if isValid(lineDiff):
                    # print(f"{line} : invalid\n{oneDropped} : valid\n{lineDiff=}")
                    # print()
                    safe += 1
                    break

    return safe

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
