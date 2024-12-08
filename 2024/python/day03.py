import math, string
import re, os
# import numpy as np
from pprint import pprint

def part1(lines):
    joinedLines = ''.join(lines)
    mulPairs = re.findall(r"mul\((\d+),(\d+)\)", joinedLines)
    prods = [int(x[0]) * int(x[1]) for x in mulPairs]
    return sum(prods)

def part2(lines):
    joinedLines = str()
    for line in lines:
        joinedLines += line.strip()
    joinedLines = "do()" + joinedLines
    # print(joinedLines)

    # split on the dos and donts
    dosAndDonts = re.sub(
            pattern=r"(do\(\)|don't\(\))",
            repl=r"\n\1",
            string=joinedLines
          )
    dosAndDonts = dosAndDonts.splitlines()
    # print(dosAndDonts)

    # filter out the donts
    dos = [x for x in dosAndDonts if x.startswith("do()") ]
    dos = ''.join(dos)
    # print(dos)

    mulPairs = re.findall(r"mul\((\d+),(\d+)\)", dos)
    prods = [int(x[0]) * int(x[1]) for x in mulPairs]
    return sum(prods)

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
