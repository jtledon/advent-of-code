import math, string
import re, os, sys
import numpy as np
import functools, itertools
from enum import Enum, IntEnum
from collections import Counter, defaultdict
from pprint import pprint

sys.path.append('..')
from utils import custom_timer

# @custom_timer
def part1(groups):
    # pprint(lines)
    winningCombination = list()
    for a, b, prize in groups:
        aX, aY = re.match(r'.*X\+(\d+).*Y\+(\d+)', a).groups()
        bX, bY = re.match(r'.*X\+(\d+).*Y\+(\d+)', b).groups()
        pX, pY = re.match(r'.*X=(\d+).*Y=(\d+)', prize).groups()
        # print(aX, bX, aY, bY)

        systemOfEq = [[int(aX), int(bX)], [int(aY), int(bY)]]
        res = [int(pX), int(pY)]
        aPresses, bPresses = np.linalg.solve(systemOfEq, res)
        # print(solution)

        if np.isclose(np.round(aPresses), aPresses) and np.isclose(np.round(bPresses), bPresses):
            winningCombination.append(round(aPresses)*3 + round(bPresses))

    return sum(winningCombination)



# @custom_timer
def part2(groups):
    # pprint(lines)
    winningCombination = list()
    for a, b, prize in groups:
        aX, aY = re.match(r'.*X\+(\d+).*Y\+(\d+)', a).groups()
        bX, bY = re.match(r'.*X\+(\d+).*Y\+(\d+)', b).groups()
        pX, pY = re.match(r'.*X=(\d+).*Y=(\d+)', prize).groups()
        # print(aX, bX, aY, bY)

        systemOfEq = [[int(aX), int(bX)], [int(aY), int(bY)]]
        res = [int(pX)+10000000000000, int(pY)+10000000000000]
        aPresses, bPresses = np.linalg.solve(systemOfEq, res)
        # print(solution)

        if math.isclose(round(aPresses), aPresses, rel_tol=1e-15) and math.isclose(round(bPresses), bPresses, rel_tol=1e-15):
            winningCombination.append(round(aPresses)*3 + round(bPresses))

    return sum(winningCombination)



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
        lines = f.read().strip().split('\n\n')
        lines = [ [ line.strip() for line in group.split('\n') ] for group in lines]

    print(part1(lines))
    print(part2(lines))
