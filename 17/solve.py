from math import prod


def count_surrounding_active(grid, pos):
    dirs = [(x, y, z) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2)]
    active = 0
    for dir in dirs:
        if dir == (0, 0, 0):
            continue
        pos_to_check = (pos[0] + dir[0], pos[1] + dir[1], pos[2] + dir[2])
        if grid.get(pos_to_check, '.') == '#':
            active += 1
    return active


def count_surrounding_active_2(grid, pos):
    dirs = [(x, y, z, a) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2) for a in range(-1, 2)]
    # dirs = [
    #     (-1, 0, 0),
    #     (1, 0, 0),
    #     (0, -1, 0),
    #     (0, 1, 0),
    #     (0, 0, -1),
    #     (0, 0, 1),
    # ]
    # print(dirs)
    active = 0
    for dir in dirs:
        if dir == (0, 0, 0, 0):
            continue
        pos_to_check = (pos[0] + dir[0], pos[1] + dir[1], pos[2] + dir[2], pos[3] + dir[3])
        if grid.get(pos_to_check, '.') == '#':
            active += 1
    return active


def print_grid(grid):
    minx = min(grid, key=lambda key: key[0])[0]
    maxx = max(grid, key=lambda key: key[0])[0]

    miny = min(grid, key=lambda key: key[1])[1]
    maxy = max(grid, key=lambda key: key[1])[1]

    minz = min(grid, key=lambda key: key[2])[2]
    maxz = max(grid, key=lambda key: key[2])[2]
    # print("i = ", i)
    for z in range(minz, maxz + 1):
        print("z = ", z)
        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                print(grid[(x, y, z)], end='')
            print()


def calc_new_grid(grid):
    new_grid = {}

    minx = min(grid, key=lambda key: key[0])[0]
    maxx = max(grid, key=lambda key: key[0])[0]

    miny = min(grid, key=lambda key: key[1])[1]
    maxy = max(grid, key=lambda key: key[1])[1]

    minz = min(grid, key=lambda key: key[2])[2]
    maxz = max(grid, key=lambda key: key[2])[2]
    for x in range(minx - 1, maxx + 2):
        for y in range(miny - 1, maxy + 2):
            for z in range(minz - 1, maxz + 2):
                pos = (x, y, z)
                active = count_surrounding_active(grid, pos)
                thing = grid.get(pos, '.')
                # print("thing = ", thing, pos)
                if grid.get(pos, '.') == '#':
                    if active in [2, 3]:
                        new_grid[pos] = '#'
                    else:
                        new_grid[pos] = '.'
                else:
                    if active == 3:
                        new_grid[pos] = '#'
                    else:
                        new_grid[pos] = '.'
    return new_grid


def calc_new_grid_2(grid):
    new_grid = {}

    minx = min(grid, key=lambda key: key[0])[0]
    maxx = max(grid, key=lambda key: key[0])[0]

    miny = min(grid, key=lambda key: key[1])[1]
    maxy = max(grid, key=lambda key: key[1])[1]

    minz = min(grid, key=lambda key: key[2])[2]
    maxz = max(grid, key=lambda key: key[2])[2]

    mina = min(grid, key=lambda key: key[3])[3]
    maxa = max(grid, key=lambda key: key[3])[3]

    for x in range(minx - 1, maxx + 2):
        for y in range(miny - 1, maxy + 2):
            for z in range(minz - 1, maxz + 2):
                for a in range(mina - 1, maxa + 2):
                    pos = (x, y, z, a)
                    active = count_surrounding_active_2(grid, pos)
                    if grid.get(pos, '.') == '#':
                        if active in [2, 3]:
                            new_grid[pos] = '#'
                        else:
                            new_grid[pos] = '.'
                    else:
                        if active == 3:
                            new_grid[pos] = '#'
                        else:
                            new_grid[pos] = '.'
    return new_grid


def solve_part_1(lines):
    grid = {}
    for y, line in enumerate(lines):
        for x, s in enumerate(line.strip()):
            grid[(x, y, 0)] = s

    # print_grid(grid)

    for i in range(6):
        grid = calc_new_grid(grid)
        # print_grid(grid)

    actives = [active for active in grid if grid[active] == '#']
    # print("Actives:", actives)

    # print("2.")
    # print(new_grid)
    #
    #
    return len(actives)


def solve_part_2(lines):
    grid = {}
    for y, line in enumerate(lines):
        for x, s in enumerate(line.strip()):
            grid[(x, y, 0, 0)] = s

    # print_grid(grid)

    for i in range(6):
        grid = calc_new_grid_2(grid)
        # print_grid(grid)

    actives = [active for active in grid if grid[active] == '#']
    # print("Actives:", actives)

    # print("2.")
    # print(new_grid)
    #
    #
    return len(actives)


def solve():
    # lines = open('easy.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()

    # print("Part 1:", solve_part_1(lines))
    print("Part 2:", solve_part_2(lines))


solve()


