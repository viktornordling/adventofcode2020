from math import prod
import re
import math
import string


def parse(line):
    return int(line)


def solve_part1(numbers):
    size = 25
    buffer = numbers[0:size]
    for n in numbers[size:]:
        sum_in_buffer = False
        for b in buffer:
            if (n - b) in buffer:
                sum_in_buffer = True
        if not sum_in_buffer:
            return n
        del buffer[0]
        buffer.append(n)


def solve_part2(numbers, part_2_n):
    nbuffer = []
    for n in numbers:
        sum = 0
        added = []
        for b in nbuffer:
            sum += b
            added.append(b)
            if sum == part_2_n:
                added.sort()
                return added[0] + added[-1]
        while sum > part_2_n:
            deleted = nbuffer[0]
            del nbuffer[0]
            sum -= deleted
        nbuffer.append(n)


def solve():
    # lines = open('easy.txt', 'r').readlines()
    lines = open('09/input.txt', 'r').readlines()

    numbers = [parse(line) for line in lines]

    part2_n = solve_part1(numbers)
    print("Part 1:", part2_n)
    print("Part 2:", solve_part2(numbers, part2_n))


solve()