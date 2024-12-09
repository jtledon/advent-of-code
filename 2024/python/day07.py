import math, string
import re, os, sys
import numpy as np
import functools, itertools
from pprint import pprint
from collections import Counter

sys.path.append('..')
from utils import custom_timer

def applyOperationPart1(target: int, currTotal: int, remainingNumbers: list[int]):
    if len(remainingNumbers) <= 1:
        a = target == currTotal * remainingNumbers[0]
        b = target == currTotal + remainingNumbers[0]
        return a or b
    front, rest = remainingNumbers[0], remainingNumbers[1:]
    return applyOperationPart1(target, currTotal * front, rest) or applyOperationPart1(target, currTotal + front, rest)

def applyOperationPart2(target: int, currTotal: int, remainingNumbers: list[int]):
    if len(remainingNumbers) <= 1:
        a = target == currTotal * remainingNumbers[0]
        b = target == currTotal + remainingNumbers[0]
        c = target == int(str(currTotal) + str(remainingNumbers[0]))
        return a or b or c
    front, rest = remainingNumbers[0], remainingNumbers[1:]
    return applyOperationPart2(target, currTotal * front, rest) or \
            applyOperationPart2(target, currTotal + front, rest) or \
            applyOperationPart2(target, int(str(currTotal) + str(remainingNumbers[0])), rest)

# @custom_timer
def part1(lines):
    matchUpCount = 0
    for line in lines:
        target, numbers = line.split(':')
        target = int(target)
        numbers = list(map(int, numbers.strip().split(' ')))

        front, rest = numbers[0], numbers[1:]
        matchUpCount += applyOperationPart1(target, front, rest) * target

    return matchUpCount



# @custom_timer
def part2(lines):
    matchUpCount = 0
    for line in lines:
        target, numbers = line.split(':')
        target = int(target)
        numbers = list(map(int, numbers.strip().split(' ')))

        front, rest = numbers[0], numbers[1:]
        matchUpCount += applyOperationPart2(target, front, rest) * target

    return matchUpCount



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
