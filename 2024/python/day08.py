import math, string
import re, os, sys
import numpy as np
import functools, itertools
from pprint import pprint
from collections import Counter
from collections import defaultdict

sys.path.append('..')
from utils import custom_timer

# @custom_timer
def part1(lines):
    freqType = defaultdict(set)
    for i, line in enumerate(lines):
        line = list(line)
        for j, symbol in enumerate(line):
            if symbol == '.':
                continue

            freqType[symbol] = freqType[symbol].union({(i, j)})
    # pprint(freqType)

    sameFreqLines = list()
    for v in freqType.values():
        sameFreqLines.extend(itertools.combinations(v, 2))

    uniqueAntinodes = set()
    for ((a, b), (x, y)) in sameFreqLines:
        diff = (x-a, y-b)
        # distances are being based off of x,y since they are the positive
        # print(a, b, x, y, diff)
        # print(f'{(x + diff[0], y + diff[1])}, {(x - 2*diff[0], y - 2*diff[1])}')
        # print()

        antinodes = { (x + diff[0], y + diff[1]), (x - 2*diff[0], y - 2*diff[1]) }
        uniqueAntinodes.update(antinodes)
        # print(uniqueAntinodes)

    # print(len(uniqueAntinodes))
    uniqueAndValid = list(filter(lambda loc:
                                 loc[0] >= 0 and
                                 loc[1] >= 0 and
                                 loc[0] < len(lines) and
                                 loc[1] < len(lines[0]),
                            uniqueAntinodes)
                          )

    return len(uniqueAndValid)



# @custom_timer
def part2(lines):
    freqType = defaultdict(set)
    for i, line in enumerate(lines):
        line = list(line)
        for j, symbol in enumerate(line):
            if symbol == '.':
                continue

            freqType[symbol] = freqType[symbol].union({(i, j)})
    # pprint(freqType)

    sameFreqLines = list()
    for v in freqType.values():
        sameFreqLines.extend(itertools.combinations(v, 2))

    uniqueAntinodes = set()
    for ((a, b), (x, y)) in sameFreqLines:
        diff = (x-a, y-b)
        # distances are being based off of x,y since they are the positive
        # print(a, b, x, y, diff)
        # print(f'{(x + diff[0], y + diff[1])}, {(x - 2*diff[0], y - 2*diff[1])}')
        # print()

        antinodes = set()
        for mul in range(-len(lines), len(lines)):
            if mul == -1:
                continue
            antinodes.update({(x + mul*diff[0], y + mul*diff[1])})
            # print(antinodes)
        uniqueAntinodes.update(antinodes)
        # print(uniqueAntinodes)

    # print(len(uniqueAntinodes))
    uniqueAndValid = list(filter(lambda loc:
                                 loc[0] >= 0 and
                                 loc[1] >= 0 and
                                 loc[0] < len(lines) and
                                 loc[1] < len(lines[0]),
                            uniqueAntinodes)
                          )

    print(uniqueAndValid)
    return len(uniqueAndValid)



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
