import math, string
import re, os, sys
import numpy as np
import functools, itertools
from pprint import pprint
from collections import Counter
from collections import defaultdict

sys.path.append('..')
from utils import custom_timer

def getPossibleStepsPt1(board, pos):
    x, y = pos
    directions = [
            ( 0,  1)
          , ( 0, -1)
          , ( 1,  0)
          , (-1,  0)
    ]

    newPos = list()
    for dx, dy in directions:
        xPrime = x+dx
        yPrime = y+dy
        if ( 0 <= xPrime < len(board)) and \
           ( 0 <= yPrime < len(board[xPrime])) and \
           (board[xPrime][yPrime] != '.'):
            newPos.append((xPrime, yPrime))

    return newPos


# @custom_timer
def part1(lines):
    matrix = [ [ c if c == '.' else int(c) for c in line ] for line in lines]
    reachablePoints = defaultdict(set)
    reachablePoints[0] = { (i, j) for i in range(len(lines)) for j in range(len(lines[i])) if (matrix[i][j] == 0) }

    # can either do this using bfs and keep a set with the most recently visited new locations
    currentHeight = 0
    while currentHeight < 9:
        for (i, j) in reachablePoints[currentHeight]:
            adjacents = getPossibleStepsPt1(matrix, (i, j))
            nextHeight = { (x, y) for x, y in adjacents if matrix[x][y] == currentHeight + 1}
            reachablePoints[currentHeight + 1].update(nextHeight)
        currentHeight += 1

    pprint(reachablePoints)
    return len(reachablePoints[9])



# @custom_timer
def part2(lines):
    return



if __name__ == "__main__":
    filename = os.path.basename(__file__)
    dayNumber = re.sub(r"^.*?(\d+)\.py$", r"\1", filename)
    yearNumber = os.path.basename(os.path.dirname(os.path.dirname(__file__)))

    inputFile = os.path.join(
            os.path.dirname(__file__),
            '../input-files/',
            f'adventofcode.com_{yearNumber}_day_{dayNumber}_input.txt.test'
            )
    inputFile = os.path.normpath(inputFile)

    with open(inputFile, 'r') as f:
        lines = f.readlines()
        lines = list(map(str.strip, lines))

    print(part1(lines))
    print(part2(lines))
