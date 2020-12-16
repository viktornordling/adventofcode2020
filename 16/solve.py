from math import prod
import re
import math
import string
from functools import reduce


def invalid(line, fields):
    values = [int(x) for x in line.split(",")]
    for x in values:
        valid_for_some_field = False
        for f in fields:
            for r in f['ranges']:
                if x >= r[0] and x <= r[1]:
                    valid_for_some_field = True
                    break
        if not valid_for_some_field:
            return x
    return -1


def solve_part_1(lines):
    parts = lines.split("\n\n")
    fields = parts[0].split("\n")
    all_fields = []
    for line in fields:
        field_name = line.split(": ")[0]
        rules = line.split(": ")[1].split(" or ")
        ranges = [(int(rule.split("-")[0]), int(rule.split("-")[1])) for rule in rules]
        all_fields.append({'name': field_name, 'ranges': ranges})

    nearby = parts[2].split("\n")
    invalids = [invalid(line, all_fields) for line in nearby[1:]]
    xx = [x for x in invalids if x != -1]
    return sum(xx)


def all_tickets_valid_in_col(valids, field, col):
    ranges = field['ranges']
    for v in valids:
        values = [int(x) for x in v.split(",")]
        col_value = values[col]
        valid = False
        for r in ranges:
            if col_value >= r[0] and col_value <= r[1]:
                valid = True
                break
        if not valid:
            return False
    return True


def assign_cols(pot_cols, assigned_cols, assigned_col_set, unassigned_col_set):
    if len(unassigned_col_set) == 0:
        return assigned_cols

    forced_cols = [col for col in pot_cols if len(pot_cols[col]) == 1]
    for f in forced_cols:
        forced_col = pot_cols[f][0]
        assigned_cols[f] = forced_col
        assigned_col_set.add(forced_col)
        unassigned_col_set.remove(forced_col)

    # remove all assigned_cols
    for f in pot_cols:
        cur = pot_cols[f]
        new_cur = [col for col in cur if col not in assigned_col_set]
        pot_cols[f] = new_cur

    return assign_cols(pot_cols, assigned_cols, assigned_col_set, unassigned_col_set)


def solve_part_2(lines):
    parts = lines.split("\n\n")
    fields = parts[0].split("\n")
    all_fields = []
    for line in fields:
        field_name = line.split(": ")[0]
        rules = line.split(": ")[1].split(" or ")
        ranges = [(int(rule.split("-")[0]), int(rule.split("-")[1])) for rule in rules]
        all_fields.append({'name': field_name, 'ranges': ranges})

    nearby = parts[2].split("\n")
    valids = [line for line in nearby[1:] if invalid(line, all_fields) == -1]

    # Maps each field to a list of cols that satisfy that field
    pot_cols = {}
    col_count = 20
    for field in all_fields:
        cols = []
        for col in range(col_count):
            if all_tickets_valid_in_col(valids, field, col):
                cols.append(col)
        pot_cols[field['name']] = cols
    assigned_cols = assign_cols(pot_cols, {}, set(), set([key for key in range(col_count)]))

    our_tick = parts[1].split("\n")
    our_vals = [int(x) for x in our_tick[1].split(",")]

    dep_vals = []
    for field in all_fields:
        if "departure" in field['name']:
            # get col pos
            col = assigned_cols[field['name']]
            # get value on our ticket
            dep_vals.append(our_vals[col])
    return prod(dep_vals)


def solve():
    # lines = open('easy.txt', 'r').read()
    lines = open('input.txt', 'r').read()

    print("Part 1:", solve_part_1(lines))
    print("Part 2:", solve_part_2(lines))


solve()


