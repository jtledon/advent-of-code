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
def part1(lines):
    id = 0
    onFileLenNumber = True
    # idLayoutRepresentation = str()
    idLayoutRepresentation = list()
    for lenCount in lines[0]:
        # idLayoutRepresentation += '.'*int(lenCount) if not onFileLenNumber else str(id)*int(lenCount)
        idLayoutRepresentation.extend(['.']*int(lenCount) if not onFileLenNumber else [str(id)]*int(lenCount))
        if onFileLenNumber:
            id += 1
        onFileLenNumber = not onFileLenNumber

    # print(idLayoutRepresentation)
    # print(''.join(idLayoutRepresentation))

    frontIdx, backIdx = 0, len(idLayoutRepresentation)-1
    while frontIdx <= backIdx:
        bothValid = True
        front, back = idLayoutRepresentation[frontIdx], idLayoutRepresentation[backIdx]

        if back == '.':
            backIdx -= 1
            bothValid = False
        if front != '.':
            frontIdx += 1
            bothValid = False

        if bothValid:
            idLayoutRepresentation[frontIdx] = idLayoutRepresentation[backIdx]
            idLayoutRepresentation[backIdx] = '.'

    # print(idLayoutRepresentation)
    return sum( int(x) * i for i, x in enumerate(idLayoutRepresentation) if x != '.' )

# @custom_timer
def part2(lines):
    id = 0
    onFileLenNumber = True
    blocks = list()
    for i, lenOfBlock in enumerate(lines[0]):
        lenOfBlock = int(lenOfBlock)

        if lenOfBlock <= 0:
            onFileLenNumber = not onFileLenNumber
            continue

        if onFileLenNumber:
            blocks.append( ('file', id, lenOfBlock) )
            id += 1
        else:
            blocks.append( ('gap', None, lenOfBlock) )

        onFileLenNumber = not onFileLenNumber
    # print(layoutRepresentation)

    backOffset = 0
    while (len(blocks) - 1 - backOffset > 0):
        backIndex = len(blocks) - 1 - backOffset
        # print(f"{backIndex=}")
        fileBlockType, fileId, fileLenOfBlock = blocks[backIndex]

        if fileBlockType == 'gap':
            backOffset += 1
            continue

        frontIndex = 0
        while (frontIndex <= backIndex):
            # print(f"{frontIndex=}")
            gapBlockType, _, gapLenOfBlock = blocks[frontIndex]
            if gapBlockType == 'file' or gapLenOfBlock < fileLenOfBlock:
                frontIndex += 1
                continue

            fileBlock = blocks.pop(backIndex)
            gapBlock = blocks.pop(frontIndex)
            blocks.insert(frontIndex, fileBlock)
            blocks.insert(frontIndex+1, (gapBlock[0], gapBlock[1], gapBlock[2]-fileLenOfBlock))
            blocks.insert(backIndex+1, (gapBlock[0], gapBlock[1], fileLenOfBlock))
            break

        backOffset += 1

    # print(blocks)

    idLayout = list()
    for block in blocks:
        idLayout.extend([block[1]] * block[2])

    # print(idLayout)
    return sum( int(x) * i for i, x in enumerate(idLayout) if x is not None )

if __name__ == "__main__":
    filename = os.path.basename(__file__)
    dayNumber = re.sub(r"^.*?(\d+)\.py$", r"\1", filename)
    yearNumber = os.path.basename(os.path.dirname(os.path.dirname(__file__)))

    inputFile = os.path.join(
            os.path.dirname(__file__),
            '../input-files/',
            # f'adventofcode.com_{}_day_{dayNumber}_input.txt'
            f'adventofcode.com_{yearNumber}_day_{dayNumber}_input.txt'
            )
    inputFile = os.path.normpath(inputFile)

    with open(inputFile, 'r') as f:
        lines = f.readlines()
        lines = list(map(str.strip, lines))

    print(part1(lines))
    print(part2(lines))
