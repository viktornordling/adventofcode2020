from itertools import count
from math import prod


def count_trees(lines, skip_x, skip_y):
    cur_x = 0
    trees = 0
    line_width = len(lines[0]) - 1
    for i in range(skip_y, len(lines), skip_y):
        line = lines[i]
        cur_x += skip_x
        cur_x = cur_x % line_width
        if (line[cur_x] == '#'):
            trees += 1
    return trees

# lines = open('easy.txt', 'r').readlines()
lines = open('input.txt', 'r').readlines()

print("Part 1:", count_trees(lines, 2, 1))

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees = [count_trees(lines, x, y) for (x, y) in slopes]
print("Part 2:", prod(trees))