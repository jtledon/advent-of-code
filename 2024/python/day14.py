import math, string
import re, os, sys
import numpy as np
import functools, itertools
from enum import Enum, IntEnum
from collections import Counter, defaultdict
from pprint import pprint

sys.path.append('..')
from utils import custom_timer

class Robot(object):
    def __init__(self, x, y, dx, dy):
        self.x: int = x # how far right, from the left wall
        self.y: int = y # how for down, from top wall
        self.dx: int = dx # amount to move to the right per iteration
        self.dy: int = dy # amount to move down per iteration

    def __repr__(self):
        return f'Robot(x={self.x}, y={self.y}, dx={self.dx}, dy={self.dy})'

def getRobots(lines):
    robots = list()
    for line in lines:
        robotData = re.match(r'^p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line)
        x, y, dx, dy = robotData.groups()
        robots.append(Robot(int(x), int(y), int(dx), int(dy)))
    return robots

# @custom_timer
def part1(lines):
    robots = getRobots(lines)
    # pprint(robots)

    # width = 11
    # height = 7
    width = 101
    height = 103
    board = np.zeros((height, width), dtype='int')

    iterations = 100
    for iter in range(iterations):
        for robot in robots:
            # print(robot.x + robot.y + robot.dx + robot.dy)
            robot.x = (robot.x + robot.dx) % width
            robot.y = (robot.y + robot.dy) % height

            if iter == iterations - 1: # last iteration, place them on the board
                board[robot.y][robot.x] = 1 + board[robot.y][robot.x]

    # print(board)
    q0 = board[:height//2, :width//2]
    q1 = board[:height//2, width//2+1:]
    q2 = board[height//2+1:, :width//2]
    q3 = board[height//2+1:, width//2+1:]
    # print(q0) ; print(q1) ; print(q2) ; print(q3)

    return q0.sum() * q1.sum() * q2.sum() * q3.sum()



# @custom_timer
np.set_printoptions(threshold=np.inf)
def part2(lines):
    robots = getRobots(lines)
    # pprint(robots)

    # width = 11 ; height = 7
    width = 101 ; height = 103

    iteration = 0
    while (True):
        # board = np.full((height, width), fill_value=' ', dtype='str')
        board = np.zeros((height, width), dtype='int')

        for robot in robots:
            # print(robot.x + robot.y + robot.dx + robot.dy)
            robot.x = (robot.x + robot.dx) % width
            robot.y = (robot.y + robot.dy) % height

            # board[robot.y][robot.x] = '#'
            board[robot.y][robot.x] = 1

        # if 500 < iteration < 126254:
        #     print(iteration)
        #     for line in board:
        #         print("".join(line))
        #     print(f'{"="*width}')
        #     input()

        left = board[:, :width//2+1]
        right = board[:, width//2:]
        # print(left); print(right)

        # if np.array_equal(left, np.fliplr(right)):
        sharedOnFlip = (left.flatten() == np.fliplr(right).flatten()).sum()
        print(sharedOnFlip)
        # if sharedOnFlip > 4850:
        #     print(board)
        #     break

        iteration += 1

    return iteration



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
