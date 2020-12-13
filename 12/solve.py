from math import prod
import re
import math
import string


def update_dir(cur_dir, angles):
    dirs = ['E', 'S', 'W', 'N']
    index = dirs.index(cur_dir)
    turns = angles / 90
    index += turns
    index = index % 4
    return dirs[int(index)]


def rotate_waypoint_90(waypoint, boat_point):
    xdiff = waypoint[0] - boat_point[0]
    ydiff = waypoint[1] - boat_point[1]
    newxdiff = 0
    newydiff = 0
    if xdiff >= 0 and ydiff >= 0:
        newxdiff = ydiff
        newydiff = -xdiff
    if xdiff >= 0 and ydiff <= 0:
        newxdiff = ydiff
        newydiff = -xdiff
    if xdiff <= 0 and ydiff <= 0:
        newxdiff = ydiff
        newydiff = -xdiff
    if xdiff <= 0 and ydiff >= 0:
        newxdiff = ydiff
        newydiff = -xdiff
    return (boat_point[0] + newxdiff, boat_point[1] + newydiff)


def rotate_waypoint(waypoint, boat_point, angles):
    turns = int(angles / 90)
    newpos = waypoint
    for i in range(turns % 4):
        newpos = rotate_waypoint_90(newpos, boat_point)
    return newpos


def solve_part1(moves):
    facing = 'E'
    pos = (0, 0)
    direction = (1, 0)
    dirs = {'E': (1, 0), 'S': (0, -1), 'W': (-1, 0), 'N': (0, 1)}
    for move in moves:
        arg = int(move[1:])
        cmd = move[0]
        if cmd == 'F':
            direction = dirs[facing]
            pos = (pos[0] + direction[0] * arg, pos[1] + direction[1] * arg)
        if cmd in ['E', 'S', 'W', 'N']:
            gg = dirs[cmd]
            pos = (pos[0] + gg[0] * arg, pos[1] + gg[1] * arg)
        if cmd == 'R':
            facing = update_dir(facing, arg)
        if cmd == 'L':
            facing = update_dir(facing, -arg)
    return abs(pos[0]) + abs(pos[1])


def solve_part2(moves):
    waypoint = (10, 1)
    pos = (0, 0)
    dirs = {'E': (1, 0), 'S': (0, -1), 'W': (-1, 0), 'N': (0, 1)}
    for move in moves:
        arg = int(move[1:])
        cmd = move[0]
        if cmd == 'F':
            direction1 = (waypoint[0] - pos[0], waypoint[1] - pos[1])
            pos = (pos[0] + direction1[0] * arg, pos[1] + direction1[1] * arg)
            waypoint = (pos[0] + direction1[0], pos[1] + direction1[1])
        if cmd in ['E', 'S', 'W', 'N']:
            gg = dirs[cmd]
            waypoint = (waypoint[0] + gg[0] * arg, waypoint[1] + gg[1] * arg)
        if cmd == 'R':
            waypoint = rotate_waypoint(waypoint, pos, arg)
        if cmd == 'L':
            waypoint = rotate_waypoint(waypoint, pos, -arg)
    return abs(pos[0]) + abs(pos[1])


def solve():
    # moves = open('easy.txt', 'r').readlines()
    moves = open('input.txt', 'r').readlines()

    print("Part 1:", solve_part1(moves))
    print("Part 2:", solve_part2(moves))


solve()
