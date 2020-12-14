from math import prod
import re
import math
import string
from functools import reduce


def apply_mask(val, mask):
    result = []
    for i, v in enumerate(val):
        if mask[i] == 'X':
            result.append(v)
        else:
            result.append(mask[i])
    return "".join(result)


def apply_mask_2(mem, mask):
    result = []
    for i, v in enumerate(mem):
        if mask[i] == 'X':
            result.append('X')
        elif mask[i] == '0':
            result.append(v)
        else:
            result.append('1')
    return "".join(result)


def solve_part_1(strings):
    mem = {}
    mask = ''
    for s in strings:
        if s.startswith("mask"):
            mask = s.split(" = ")[1]
        else:
            parts = s.split(" = ")
            adr = int(parts[0].replace("mem[", "").replace("]", ""))
            val = int(parts[1])
            masked = apply_mask(format(val, '036b'), mask)
            mem[adr] = masked

    sum = 0
    for k in mem:
        val = mem[k]
        intval = int(val, 2)
        sum += intval
    return sum


def get_adrs(masked, cur_pos):
    mlist = [x for x in masked]
    if cur_pos == 36:
        return [masked]
    if masked[cur_pos] == 'X':
        mlist[cur_pos] = '0'
        subs0 = get_adrs("".join(mlist), cur_pos + 1)
        mlist[cur_pos] = '1'
        subs1 = get_adrs("".join(mlist), cur_pos + 1)
        return subs0 + subs1
    else:
        return get_adrs(masked, cur_pos + 1)


def solve_part_2(strings):
    mem = {}
    mask = ''
    for s in strings:
        if s.startswith("mask"):
            mask = s.split(" = ")[1]
        else:
            parts = s.split(" = ")
            adr = int(parts[0].replace("mem[", "").replace("]", ""))
            val = format(int(parts[1]), '036b')
            masked = apply_mask_2(format(adr, '036b'), mask)
            adrs = get_adrs(masked, 0)
            for ad in adrs:
                mem[ad] = val

    sum = 0
    for k in mem:
        val = mem[k]
        intval = int(val, 2)
        sum += intval
    return sum


def solve():
    # strings = open('easy.txt', 'r').readlines()
    strings = open('input.txt', 'r').readlines()
    print("Part 1:", solve_part_1(strings))
    print("Part 2:", solve_part_2(strings))


solve()
