import math, string
import re, os
# import numpy as np
from pprint import pprint
import functools, itertools

def part1(lines):
    splitAt = lines.index('')
    rules = lines[:splitAt]
    rules = map(lambda x: x.split('|'), rules)
    rules = list(map(lambda x: list(map(int, x)), rules))
    # print(rules)

    pages = lines[splitAt+1:]
    pages = map(lambda x: x.split(','), pages)
    pages = list(map(lambda x: list(map(int, x)), pages))
    # pprint(pages)

    medianSum = 0
    for page in pages:
        for (num1, num2) in rules:
            if num1 not in page or num2 not in page:
                # print(f"missing rule number in page: {num1=} {num2=} {page=}")
                continue

            inOrder = page.index(num1) < page.index(num2)
            # print(page.index(num1), page.index(num2), inOrder)
            if not inOrder:
                # print(f"{page=} invalid because rules out of order: {num1=}|{num2=}")
                break
        else:
            medianSum += page[len(page)//2]

    return medianSum

def ruleSort(a, b):
    pass

global rulesGlobal

def part2(lines):
    splitAt = lines.index('')
    rules = lines[:splitAt]
    rules = map(lambda x: x.split('|'), rules)
    rules = list(map(lambda x: list(map(int, x)), rules))
    # print(rules)

    pages = lines[splitAt+1:]
    pages = map(lambda x: x.split(','), pages)
    pages = list(map(lambda x: list(map(int, x)), pages))
    # pprint(pages)

    medianSum = 0
    for page in pages:
        for (num1, num2) in rules:
            if num1 not in page or num2 not in page:
                # print(f"missing rule number in page: {num1=} {num2=} {page=}")
                continue

            inOrder = page.index(num1) < page.index(num2)
            # print(page.index(num1), page.index(num2), inOrder)

            if inOrder:
                # print(f"{page=} skip this rule, its in order: {num1=}|{num2=}")
                continue

            # num2 is too late. put it JUST before num1
            page = page[:page.index(num1)] + page[page.index(num1)+1:]
            page.insert(page.index(num2), num1)

        else:
            medianSum += page[len(page)//2]

    return medianSum

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