from math import prod
import re
import math

def binary_search(rows, start, stop):
    if start == stop:
        return start
    head, *tail = rows
    if head == 'F':
        return binary_search(tail, start, start + ((stop - start) // 2))
    else:
        return binary_search(tail, start + math.ceil((stop - start) / 2), stop)

def get_row(boarding_pass):
    rows = boarding_pass[0:7]
    return binary_search(rows, 0, 127)

def get_col(boarding_pass):
    col = boarding_pass[7:10]
    return binary_search(col.replace("L", "F"), 0, 7)

def get_seat_id(boarding_pass):
    row = get_row(boarding_pass)
    col = get_col(boarding_pass)
    return row * 8 + col

# lines = open('easy.txt', 'r').readlines()
lines = open('input.txt', 'r').readlines()
seat_ids = set([get_seat_id(boarding_pass) for boarding_pass in lines])
print("Part 1:", max(seat_ids))

for i in range(0, 127):
    for j in range(0, 7):
        seat_id = i * 8 + j
        if seat_id not in seat_ids and seat_id - 1 in seat_ids and seat_id + 1 in seat_ids:
            print("Part 2:", seat_id)
