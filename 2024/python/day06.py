import math, string
import re, os, sys
import numpy as np
import functools, itertools
from enum import IntEnum
import time
from pprint import pprint
from collections import Counter
from collections import defaultdict

sys.path.append('..')
from utils import custom_timer

class Directions(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    NONE = 4

directionMove = {
        Directions.UP: (-1, 0),
        Directions.RIGHT: (0, 1),
        Directions.DOWN: (1, 0),
        Directions.LEFT: (0, -1),
        Directions.NONE: (0, 0)
}

def turn(dir: Directions):
    # print(f"{dir=}")
    output = Directions((dir.value + 1) % 4)
    # print(f"{output=}")
    return output

# dir = Directions.UP
# for _ in range(4):
#     dir = turn(dir)


# return the new position
def takeAction(board, location, direction):
    step = directionMove[direction]
    attemptedNewPos = (location[0] + step[0], location[1] + step[1])
    if board[attemptedNewPos[0], attemptedNewPos[1]] == '#':
        return location, turn(direction)
    return attemptedNewPos, direction

def onEdgeAndFacingOut(board, pos, dir):
    if pos[0] <= 0 and dir == Directions.LEFT: # on the left edge and going left
        return True
    if pos[1] <= 0 and dir == Directions.UP: # on the top edge and going up
        return True
    if pos[0] >= len(board) - 1 and dir == Directions.DOWN: # on the right edge and going right
        return True
    if pos[1] >= len(board[pos[0]]) - 1 and dir == Directions.RIGHT: # on the right edge and going right
        return True
    return False

# @custom_timer
def getStartInfo(board):
    startPos = (-1, -1)
    startDir = Directions.NONE
    for i, row in enumerate(board):
        for j, locationType in enumerate(row):
            if locationType in ('^', '>', '<', 'v', 'V'):
                startPos = (i, j)
                match locationType:
                    case '^':
                        startDir = Directions.UP
                    case '>':
                        startDir = Directions.RIGHT
                    case '<':
                        startDir = Directions.LEFT
                    case x if x in ('v', 'V'):
                        startDir = Directions.DOWN
                    case _:
                        startDir = Directions.NONE
    # print(startPos, startDir)
    # print(board[startPos[0], startPos[1]])
    return startPos, startDir

def printBoard(board):
    for line in board:
        print(''.join(line))
    print()


# @custom_timer
def part1(lines):
    board = np.array([list(x) for x in lines])
    currentPos, currentDir = getStartInfo(board)

    visitedCoords = set()
    while (not onEdgeAndFacingOut(board, currentPos, currentDir)):
        visitedCoords.add(currentPos)
        board[currentPos[0], currentPos[1]] = 'x'
        currentPos, currentDir = takeAction(board, currentPos, currentDir)
    board[currentPos[0], currentPos[1]] = 'x'
    visitedCoords.add(currentPos)

    return len(visitedCoords)



# @custom_timer
def part2(lines):
    board = np.array([list(x) for x in lines])

    currentPos, currentDir = getStartInfo(board)
    visitedCoords = set()
    while (not onEdgeAndFacingOut(board, currentPos, currentDir)):
        visitedCoords.add(currentPos)
        currentPos, currentDir = takeAction(board, currentPos, currentDir)
    visitedCoords.add(currentPos)

    obstructedBoards = list()
    for i, j in visitedCoords:
        newBoard = board.copy()
        newBoard[i, j] = '#'
        obstructedBoards.append(newBoard)
    # print(len(obstructedBoards))

    successfullyLooping = 0
    for num, board in enumerate(obstructedBoards):
        posAndDirDict = defaultdict(int)
        currentPos, currentDir = getStartInfo(board)
        while (not onEdgeAndFacingOut(board, currentPos, currentDir)):
            posAndDirDict[(currentPos, currentDir)] = posAndDirDict[(currentPos, currentDir)] + 1
            board[currentPos[0], currentPos[1]] = 'x'
            currentPos, currentDir = takeAction(board, currentPos, currentDir)
            if posAndDirDict[(currentPos, currentDir)] > 1:
                successfullyLooping += 1
                break
        board[currentPos[0], currentPos[1]] = 'x'

        print(num)

    return successfullyLooping

# improvements
#   determine loop when we are in the same direction in the same position
#   only consider obstruction locations on the original path


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
