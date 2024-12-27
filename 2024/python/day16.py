import math, string
import re, os, sys
from typing import NewType
import numpy as np
import functools, itertools
from enum import Enum, IntEnum
from collections import Counter, defaultdict
import copy
from pprint import pprint

sys.path.append('..')
from utils import custom_timer


def getPathScore(path, lines):
    linesCopy = copy.deepcopy(lines)
    for i, j in path:
        if linesCopy[i][j] == '.':
            linesCopy[i][j] = 'O'
    # pprint([''.join(line) for line in linesCopy])

    changePath = list()
    for i in range(1, len(path)):
        x, y = path[i]
        px, py = path[i-1]
        dx, dy = x - px, y - py
        changePath.append([dx, dy])

    groupings = [ changePath[i-1:i+1] for i in range(1, len(changePath)) ]

    turnCount = 0
    for a, b in groupings:
        if a != b:
            turnCount += 1

    score =  len(path) + turnCount * 1000

    return score + 1000 - 1 # +1000 bc theres a "turn" on the first step and -1 bc we dont count one of the final steps

# @custom_timer
def part1(lines):
    adjacency = defaultdict(set)
    start = (0, 0)
    end = (0, 0)
    for i, line in enumerate(lines):
        for j, typ in enumerate(line):
            if typ == '#': continue
            elif typ == 'S': start = (i, j)
            elif typ == 'E': end = (i, j)
            dirs = [
                    (1, 0),
                    (-1, 0),
                    (0, 1),
                    (0, -1),
            ]
            adjacency[(i, j)] = { (i+di, j+dj) for di, dj in dirs if 0 <= i+di < len(lines) and 0 <= j+dj < len(lines[i]) and lines[i+di][j+dj] != '#' }

    visited = set()
    # toVisit = {((start),)} # set of tuples containing tuples
    toVisit = [[(start),]] # set of tuples containing tuples
    # print(toVisit)

    completePaths = set()
    while len(toVisit) > 0:
        nextIterToVisit = list()
        for currentPath in toVisit:
            # currentPath = toVisit.pop()
            currentPos = currentPath[-1]
            visited.add(currentPos)
            if currentPos == end:
                completePaths.add(tuple(currentPath))

            reachablePos = adjacency[currentPos]
            # newPositions = reachablePos.difference(visited) # we dont care if weve visited it before, we care about the shortest path based on the math
            newPositions = { tup for tup in reachablePos if tup not in currentPath }
            nextIterToVisit.extend([ currentPath + [newPos] for newPos in newPositions ])
            print(len(toVisit))
        toVisit = nextIterToVisit
    # print(fastestPath)

    # for path in completePaths:
    #     linesCopy = copy.deepcopy(lines)
    #     for i, j in path:
    #         if linesCopy[i][j] == '.':
    #             linesCopy[i][j] = 'O'
    #     pprint([''.join(line) for line in linesCopy])
    #     print()

    scores = [getPathScore(path, lines) for path in completePaths]
    return min(scores)




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
            f'adventofcode.com_{yearNumber}_day_{dayNumber}_input.txt'
            )
    inputFile = os.path.normpath(inputFile)

    with open(inputFile, 'r') as f:
        lines = f.readlines()
        # lines = list(map(str.strip, lines))
        lines = [ list(line.strip()) for line in lines ]

    print(part1(lines))
    print(part2(lines))
