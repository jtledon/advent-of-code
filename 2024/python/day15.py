import math, string
import re, os, sys
import numpy as np
import functools, itertools
from enum import Enum, IntEnum
from collections import Counter, defaultdict
from pprint import pprint

sys.path.append('..')
from utils import custom_timer

dirToMotion = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0)
}

# @custom_timer
def part1(board, instructions):
    robotPos = (0, 0)
    for i, line in enumerate(board):
        for j, typ in enumerate(line):
            if typ == '@':
                robotPos = (i, j)

    for motion in instructions:
        x, y = robotPos
        dx, dy = dirToMotion[motion]
        xPrime, yPrime = x+dx, y+dy
        if board[xPrime, yPrime] == '#':
            continue
        elif board[xPrime, yPrime] == '.':
            robotPos = (xPrime, yPrime)
            board[xPrime, yPrime] = '@'
            board[x, y] = '.'
        elif board[xPrime, yPrime] == 'O':
            iter = 1
            movables = [(x, y)]
            while True:
                xBox, yBox = x + iter*dx, y + iter*dy
                if board[xBox, yBox] == '#':
                    movables = list()
                    break
                elif board[xBox, yBox] == '.':
                    break
                elif board[xBox, yBox] == 'O':
                    movables.append((xBox, yBox))
                else:
                    print('unknown block')

                iter += 1

            for movableX, movableY in reversed(movables):
                board[movableX+dx, movableY+dy] = board[movableX, movableY]
            if len(movables) > 0:
                board[x, y] = '.'
                robotPos = (xPrime, yPrime)

        else:
            print(f'unknown block: {board[xPrime, yPrime]}')

    total = 0
    for i, line in enumerate(board):
        for j, typ in enumerate(line):
            if typ == 'O':
                total += 100*i + j

    return total


def printBoard(board):
    for line in board:
        print(''.join(line))
    print()
    return

# @custom_timer
def part2(board, instructions):
    bigBoard = list()
    for i, line in enumerate(board):
        bigLine = list()
        for j, typ in enumerate(line):
            if typ == '@':
                bigLine.extend(['@', '.'])
            elif typ == '#':
                bigLine.extend(['#', '#'])
            elif typ == 'O':
                bigLine.extend(['[', ']'])
            elif typ == '.':
                bigLine.extend(['.', '.'])
            else:
                print(f'unknown type: {typ}')
        bigBoard.append(np.array(bigLine))
    bigBoard = np.array(bigBoard)
    printBoard(bigBoard)

    robotPos = (0, 0)
    for i, line in enumerate(bigBoard):
        for j, typ in enumerate(line):
            if typ == '@':
                robotPos = (i, j)

    for motion in instructions:
        printBoard(bigBoard)
        print(motion)
        x, y = robotPos
        dx, dy = dirToMotion[motion]
        xPrime, yPrime = x+dx, y+dy
        if bigBoard[xPrime, yPrime] == '#':
            continue
        elif bigBoard[xPrime, yPrime] == '.':
            robotPos = (xPrime, yPrime)
            bigBoard[xPrime, yPrime] = '@'
            bigBoard[x, y] = '.'
        elif bigBoard[xPrime, yPrime] == '[' or bigBoard[xPrime, yPrime] == ']':
            unexplored = {(x, y, '@')}
            explored = set()
            while len(unexplored) > 0:
                exploring = unexplored.pop()
                explored.add(exploring)
                xExploring, yExploring, _ = exploring
                xNew, yNew = xExploring + dx, yExploring + dy
                match bigBoard[xNew, yNew]:
                    case '#':
                        unexplored = list()
                        explored = list()
                        break
                    case '.':
                        continue
                    case '[':
                        unexplored.update({ s for s in [(xNew, yNew, '['), (xNew, yNew + 1, ']')] if s not in unexplored and s not in explored})
                    case ']':
                        unexplored.update({ s for s in [(xNew, yNew, ']'), (xNew, yNew - 1, '[')] if s not in unexplored and s not in explored})
                    case _:
                        print('unknown block')

            for movableX, movableY, typ in explored:
                bigBoard[movableX+dx, movableY+dy] = typ
                bigBoard[movableX, movableY] = '.' # this is an issue. I might be writing over one I already set here
            if len(explored) > 0:
                # bigBoard[x, y] = '.'
                robotPos = (xPrime, yPrime)

        else:
            print(f'unknown block: {bigBoard[xPrime, yPrime]}')

    total = 0
    for i, line in enumerate(bigBoard):
        for j, typ in enumerate(line):
            if typ == '[':
                total += 100*i + j

    return total



if __name__ == "__main__":
    filename = os.path.basename(__file__)
    dayNumber = re.sub(r"^.*?(\d+)\.py$", r"\1", filename)
    yearNumber = os.path.basename(os.path.dirname(os.path.dirname(__file__)))

    inputFile = os.path.join(
            os.path.dirname(__file__),
            '../input-files/',
            # f'adventofcode.com_{yearNumber}_day_{dayNumber}_input.txt'
            f'adventofcode.com_{yearNumber}_day_{dayNumber}_input.txt.test3'
            )
    inputFile = os.path.normpath(inputFile)

    with open(inputFile, 'r') as f:
        board, instructions = f.read().split('\n\n')
        board = np.array([ np.array(list(line.strip())) for line in board.split('\n') ])
        instructions = ''.join( [ line.strip() for line in instructions.split() ] )

    print(part1(board.copy(), instructions))
    print(part2(board.copy(), instructions))
