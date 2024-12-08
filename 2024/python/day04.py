import math, string
import re, os
import numpy as np
from pprint import pprint
import functools, itertools

def part1(lines):
    lines = np.array([list(x) for x in lines])
    variations = list()

    # get all the rows and cols
    for _ in range(4):
        lines = np.rot90(lines)
        # variations.append("".join(lines.flatten()))
        variations.append(lines)


    # get all the diagonals
    for _ in range(4):
        diagonalsList = list()
        for i in range(
                -(len(lines) - 1),
                 len(lines)
                ):
            diag = np.diagonal(lines, offset=i)
            diagonalsList.append(diag)

        variations.append(diagonalsList)
        lines = np.rot90(lines) # , k=2)

    # search for instances of XMAS
    xmasCount = 0
    for groups in variations:
        for line in groups:
            matches = re.findall(r'XMAS', ''.join(line))
            xmasCount += len(matches)

    return xmasCount


def part2(lines):
    lines = np.array([list(x) for x in lines])

    xs = 0
    for i, row in enumerate(lines):
        if (i <= 0) or (i >= len(lines) - 1):
            continue
        for j, col in enumerate(row):
            if (j <= 0) or (j >= len(row) - 1):
                continue

            section = lines[i-1:i+1+1, j-1:j+1+1]
            topLeftBottomRight = "".join(np.diagonal(section))
            topLeftBottomRightMatch = "MAS" == topLeftBottomRight or "MAS" == ''.join(reversed(topLeftBottomRight))

            bottomLeftTopRight = "".join(np.diagonal(np.rot90(section)))
            bottomLeftTopRightMatch = "MAS" == bottomLeftTopRight or "MAS" == ''.join(reversed(bottomLeftTopRight))

            xs += topLeftBottomRightMatch and bottomLeftTopRightMatch

    return xs

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
