from math import prod
import re
import math
import string
from functools import reduce


def first_after(earliest, bus_time):
    t = bus_time['bus_time']
    splits = earliest // t
    next = splits * t + t
    return {'bus_id': bus_time['bus_id'], 'diff': next - earliest}


def solve_part_1(earliest, buses):
    busx = buses.split(",")
    bus = [{'bus_id': int(x), 'bus_time': int(x)} for index, x in enumerate(busx) if x != 'x']
    nexts = [first_after(earliest, x) for x in bus]
    best = min(nexts, key=lambda n: n['diff'])
    print("Part 1:", best['bus_id'] * best['diff'])


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def solve_part_2(buses):
    busx = buses.split(",")
    bus = [{'bus_id': index, 'bus_time': int(x)} for index, x in enumerate(busx) if x != 'x']
    n = [b['bus_time'] for b in bus]
    a = [-b['bus_id'] for b in bus]
    x = chinese_remainder(n, a)
    print("Part 2:", x)


def solve():
    # details = open('easy.txt', 'r').readlines()
    details = open('input.txt', 'r').readlines()
    solve_part_1(int(details[0]), details[1])
    solve_part_2(details[1])


solve()
