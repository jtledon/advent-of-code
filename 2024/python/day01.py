import math, string
import re, os, sys
import numpy as np
from pprint import pprint

sys.path.append('..')
from utils import custom_timer

@custom_timer
def part1(lines):
    pairs = map(lambda x: re.split(r"\s+", x), lines)

    left = list()
    right = list()
    for pair in pairs:
        left.append(int(pair[0]))
        right.append(int(pair[1]))

    left.sort()
    right.sort()
    matching = zip(left, right)

    diff = map(lambda x: abs(x[0]-x[1]), matching)

    return sum(diff)

@custom_timer
def part1v2(lines):
    pairs = np.array([list(map(int, x.strip().split('   '))) for x in lines])
    matched = zip(sorted(pairs[:,0]), sorted(pairs[:,1]))
    diff = [abs(x[0] - x[1]) for x in matched]
    return sum(diff)

def part2(lines):
    pairs = map(lambda x: re.split(r"\s+", x), lines)

    left = list()
    right = list()
    for pair in pairs:
        left.append(int(pair[0]))
        right.append(int(pair[1]))

    counts = [(x, right.count(x)) for x in left]
    similarityScores = map(math.prod, counts)

    return sum(similarityScores)

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
    print(part1v2(lines))
    print(part2(lines))
