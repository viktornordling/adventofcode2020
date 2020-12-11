from math import prod
import re
import math
import string


def print_matrix(matrix: dict[tuple[int, int]: string]):
    print(matrix_to_string(matrix))


def matrix_to_string(matrix: dict[tuple[int, int]: string]):
    rows = max(matrix.keys(), key=lambda pair: pair[0])[0] + 1
    cols = max(matrix.keys(), key=lambda pair: pair[1])[1] + 1
    s = ''
    for r in range(rows):
        for c in range(cols):
            seat = matrix.get((r, c), '.')
            s += seat
        s += '\n'
    return s


def count_occupied_seats(seats: dict[tuple[int, int]: string], pos):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return len([dir for dir in directions if seats.get((pos[0] + dir[0], pos[1] + dir[1]), None) == '#'])


def count_occ_seats_2(seats: dict[tuple[int, int]: string], pos):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    occ = 0
    for d in directions:
        seat = '!'
        rr = pos[0]
        cc = pos[1]
        while seat is not None:
            p = (rr + d[0], cc + d[1])
            rr = rr + d[0]
            cc = cc + d[1]
            seat = seats.get(p, None)
            if seat == '#':
                occ += 1
                break
            elif seat == 'L':
                break
    return occ


def update_seats(seats: dict[tuple[int, int]: string]):
    rows = max(seats.keys(), key=lambda pair: pair[0])[0] + 1
    cols = max(seats.keys(), key=lambda pair: pair[1])[1] + 1
    new_seats = {}

    for r in range(rows):
        for c in range(cols):
            seat = seats.get((r, c), None)
            occ_seats = count_occ_seats(seats, (r, c))
            if seat == 'L' and occ_seats == 0:
                new_seats[(r, c)] = '#'
            elif seat == '#' and occ_seats >= 4:
                new_seats[(r, c)] = 'L'
            else:
                new_seats[(r, c)] = seat
    return new_seats


def update_seats_2(seats: dict[tuple[int, int]: string]):
    rows = max(seats.keys(), key=lambda pair: pair[0])[0] + 1
    cols = max(seats.keys(), key=lambda pair: pair[1])[1] + 1
    new_seats = {}

    for r in range(rows):
        for c in range(cols):
            seat = seats.get((r, c), None)
            occ_seats = count_occ_seats_2(seats, (r, c))
            if seat == 'L' and occ_seats == 0:
                new_seats[(r, c)] = '#'
            elif seat == '#' and occ_seats >= 5:
                new_seats[(r, c)] = 'L'
            else:
                new_seats[(r, c)] = seat
    return new_seats


def solve_part1(layout_input):
    seats = {}
    for row_index in range(len(layout_input)):
        row = layout_input[row_index]
        for col_index in range(len(row) - 1):
            char = row[col_index]
            seats[(row_index, col_index)] = char
    old_seats = ""
    new_seats = seats
    while True:
        new_seats = update_seats(new_seats)
        seats_to_string = matrix_to_string(new_seats)
        if seats_to_string == old_seats:
            print("Part 1:", len([s for s in new_seats if new_seats[s] == '#']))
            return
        old_seats = seats_to_string


def solve_part2(layout_input):
    seats = {}
    for row_index in range(len(layout_input)):
        row = layout_input[row_index]
        for col_index in range(len(row) - 1):
            char = row[col_index]
            seats[(row_index, col_index)] = char
    old_seats = ""
    new_seats = seats
    while True:
        new_seats = update_seats_2(new_seats)
        seats_to_string = matrix_to_string(new_seats)
        if seats_to_string == old_seats:
            print("Part 2:", len([s for s in new_seats if new_seats[s] == '#']))
            return
        old_seats = seats_to_string


def solve():
    # seats = open('easy.txt', 'r').readlines()
    seats = open('input.txt', 'r').readlines()

    solve_part1(seats)
    solve_part2(seats)


solve()
