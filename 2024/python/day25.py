import math, string
import re, os, sys
import numpy as np
import functools, itertools
from enum import Enum, IntEnum
from collections import Counter, defaultdict
from pprint import pprint

sys.path.append("..")
from utils import custom_timer


# @custom_timer
def part1(groups):
    locks = list()
    keys = list()
    for group in groups:
        group = np.array([list(line) for line in group])

        groupType = list()
        if all([topChar == "#" for topChar in group[0]]) and \
           all([botChar == "." for botChar in group[-1]]):
            groupType = locks
        elif all([topChar == "." for topChar in group[0]]) and \
             all([botChar == "#" for botChar in group[-1]]):
            groupType = keys
        else:
            pass

        heights = list()
        for column in [group[:, i] for i in range(len(group[0]))]:
            matches = re.match(r"^#+|^\.+", "".join(column))
            heights.append(matches.span()[1])
        groupType.append(heights)

    match = 0
    for key in keys:
        for lock in locks:
            for pinPos in range(len(key)):
                if key[pinPos] < lock[pinPos]: # if the key has less open space up top than the lock has blocking spaces
                    break
            else:
                match += 1

    return match


# @custom_timer
def part2(lines):
    return


if __name__ == "__main__":
    filename = os.path.basename(__file__)
    dayNumber = re.sub(r"^.*?(\d+)\.py$", r"\1", filename)
    yearNumber = os.path.basename(os.path.dirname(os.path.dirname(__file__)))

    inputFile = os.path.join(
        os.path.dirname(__file__),
        "../input-files/",
        f"adventofcode.com_{yearNumber}_day_{dayNumber}_input.txt",
        # f"adventofcode.com_{yearNumber}_day_{dayNumber}_input.txt.test",
    )
    inputFile = os.path.normpath(inputFile)

    with open(inputFile, "r") as f:
        lines = f.read()
        lines = lines.split("\n\n")
        lines = [np.array(list(line.strip().split())) for line in lines]

    print(part1(lines))
    print(part2(lines))
