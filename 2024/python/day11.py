import math, string
import re, os, sys
import numpy as np
import functools, itertools
from enum import Enum, IntEnum
from collections import Counter, defaultdict
from pprint import pprint

sys.path.append('..')
from utils import custom_timer

@custom_timer
def part1(lines):
    numbers = [ int(x) for x in lines[0].split() ]

    iterations = 25
    for _ in range(iterations):
        tempNumbers = list()
        iOffset = 0
        for i, number in enumerate(numbers):
            if number == 0:
                tempNumbers.insert(i + iOffset, 1)
            elif len(str(number)) % 2 == 0:
                left = str(number)[:len(str(number))//2]
                right = str(number)[len(str(number))//2:]
                # numbers[i] = int(right)
                # numbers.insert(i, int(left))
                tempNumbers.insert(i + iOffset, int(right))
                tempNumbers.insert(i + iOffset, int(left))
                iOffset += 1
            else:
                # numbers[i] = number * 2024
                tempNumbers.insert(i + iOffset, number * 2024)
        numbers = tempNumbers

    return len(numbers)


@functools.cache
def applyRules(num, depth):
    if depth == 0:
        return 1

    if num == 0:
        return applyRules(1, depth - 1)
    elif len(str(num)) % 2 == 0:
        left = str(num)[:len(str(num))//2]
        right = str(num)[len(str(num))//2:]
        return applyRules(int(left), depth - 1) + applyRules(int(right), depth - 1)
    else:
        return applyRules(num * 2024, depth - 1)

@custom_timer
def part2(lines):
    numbers = [ int(x) for x in lines[0].split() ]

    iterations = 75
    total = 0
    for number in numbers:
        total += applyRules(number, iterations)

    return total



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
