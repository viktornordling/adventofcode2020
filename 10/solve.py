from math import prod
import re
import math
import string


def dfs(graph, cur, seen, all_set):
    seen.add(cur)
    if seen == all_set:
        last = -10
        ones = 0
        threes = 0
        for s in sorted(seen):
            if s - last == 1:
                ones += 1
            elif s - last == 3:
                threes += 1
            last = s
        print("Part 1:", ones * threes)
        return True
    children = graph[cur]
    for child in children:
        saw_all = dfs(graph, child, seen, all_set)
        if saw_all:
            return True
    return False


def solve_part1(numbers):
    graph = {}
    snumbers = set(numbers)
    for n in numbers:
        graph[n] = [item for item in [n + 1, n + 2, n + 3] if item in snumbers]
    dfs(graph, 0, set(), set(numbers))


def topo_order(graph, start, all_nodes):
    topo = []
    seen = set()

    def dfs(cur):
        seen.add(cur)
        children = set(graph[cur]) - seen
        for child in children:
            dfs(child)
        topo.append(cur)

    dfs(start)

    if len(seen) == len(all_nodes):
        return topo
    else:
        print("Oh man.")


def solve_part2(numbers, goal):
    graph = {}
    snumbers = set(numbers)
    for n in numbers:
        graph[n] = [item for item in [n + 1, n + 2, n + 3] if item in snumbers]

    topological_order = topo_order(graph, 0, snumbers)
    ways = {goal: 1}
    for n in topological_order[1:]:
        children = graph[n]
        tot = 0
        for child in children:
            tot += ways[child]
        ways[n] = tot

    print("Part 2:", ways[0])


def solve():
    # lines = open('easy.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()

    jolts = [int(line) for line in lines]

    solve_part1(jolts + [0, max(jolts) + 3])
    solve_part2(jolts + [0, max(jolts) + 3], max(jolts) + 3)


solve()
