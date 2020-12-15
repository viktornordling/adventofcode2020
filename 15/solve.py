from math import prod
import re
import math
import string
from functools import reduce


def solve_part_1():
    age_and_occs = {}
    # startings = [0, 3, 6]
    startings = [16, 1, 0, 18, 12, 14, 19]
    last = -1
    for turn in range(30000000):
        if turn % 1000000 == 0:
            print("Turn is ", turn + 1)
        if turn < len(startings):
            print("{} is spoken:".format(startings[turn]))
            last = startings[turn]
            age_and_occs[last] = {'turn': turn, 'times': [turn]}
        else:
            ll = 0
            if age_and_occs.get(last, None) is not None:
                ll = len(age_and_occs[last]['times'])
            if age_and_occs.get(last, None) is not None and ll > 1:
                age_of_last = age_and_occs[last]['times'][-1] - age_and_occs[last]['times'][-2]
                if turn > 30000000 - 100:
                    print(age_of_last, "is spoken")
                last = age_of_last
                turns_of_new_x = age_and_occs.get(last, None)
                if turns_of_new_x is not None:
                    tt = turns_of_new_x['times']
                    tt.append(turn)
                    age_and_occs[last] = {'turn': turn, 'times': tt}
                else:
                    turns_of_new = [turn]
                    age_and_occs[last] = {'turn': turn, 'times': turns_of_new}
            else:
                if turn > 30000000 - 100:
                    print("0 is spoken")
                last = 0
                turns_of_new_x = age_and_occs.get(0, None)
                if turns_of_new_x is not None:
                    tt = turns_of_new_x['times']
                    tt.append(turn)
                    age_and_occs[last] = {'turn': 0, 'times': tt}
                else:
                    turns_of_new = [turn]
                    age_and_occs[last] = {'turn': 0, 'times': turns_of_new}

    return 1


def solve_part_2(strings):
    return 2


def solve():
    # strings = open('easy.txt', 'r').readlines()
    # strings = open('input.txt', 'r').readlines()
    print("Part 1:", solve_part_1())
    # print("Part 2:", solve_part_2(strings))


solve()


