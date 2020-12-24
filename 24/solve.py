from collections import deque


class Tile:
    _black = False

    def flip(self):
        self._black = not self._black

    def color(self):
        if self._black:
            return "black"
        return "white"


def solve_part_1(lines):
    start_tile = Tile()
    tile_map = {(0, 0): start_tile}
    for line in lines:
        ref_tile = start_tile
        pos_x = 0
        pos_y = 0
        pos = 0
        while pos < len(line):
            if line[pos:].startswith('se'):
                if pos_y % 2 == 0:
                    pos_x += 1
                pos_y -= 1
                pos += 2
            elif line[pos:].startswith('sw'):
                if pos_y % 2 == 1:
                    pos_x -= 1
                pos_y -= 1
                pos += 2
            elif line[pos:].startswith('nw'):
                if pos_y % 2 == 1:
                    pos_x -= 1
                pos_y += 1
                pos += 2
            elif line[pos:].startswith('ne'):
                if pos_y % 2 == 0:
                    pos_x += 1
                pos_y += 1
                pos += 2
            elif line[pos:].startswith('e'):
                pos_x += 1
                pos += 1
            elif line[pos:].startswith('w'):
                pos_x -= 1
                pos += 1
        ref_tile = tile_map.get((pos_x, pos_y), Tile())
        ref_tile.flip()
        tile_map[(pos_x, pos_y)] = ref_tile
    return tile_map


def count_adjacent_black_and_white(tile_pos, tile_map):
    east_incr = 0
    west_incr = 0
    if tile_pos[1] % 2 == 0:
        east_incr = 1
    if tile_pos[1] % 2 == 1:
        west_incr = 1
    adjacent_positions = [
        (tile_pos[0] + 1, tile_pos[1]),  # w
        (tile_pos[0] - 1, tile_pos[1]),  # e
        (tile_pos[0] + west_incr, tile_pos[1] - 1),  # sw
        (tile_pos[0] + east_incr, tile_pos[1] - 1),  # se
        (tile_pos[0] + west_incr, tile_pos[1] + 1),  # nw
        (tile_pos[0] + east_incr, tile_pos[1] + 1),  # ne
    ]
    missing_tile_ids = [adj_pos for adj_pos in adjacent_positions if tile_map.get(adj_pos) is None]
    # for tile_id in missing_tile_ids:
    #     new_tile = Tile()
    #     tile_map[tile_id] = new_tile
    adjacents = [tile_map[adj_pos] for adj_pos in adjacent_positions if tile_map.get(adj_pos) is not None]
    blacks = len([tile for tile in adjacents if tile.color() == 'black'])
    whites = len([tile for tile in adjacents if tile.color() == 'white']) + len(missing_tile_ids)
    return blacks, whites


def print_grid(tile_map):
    max_y = max(tile_map, key=lambda tile_key: tile_key[1])[1]
    min_y = min(tile_map, key=lambda tile_key: tile_key[1])[1]
    min_x = min(tile_map, key=lambda tile_key: tile_key[0])[0]
    max_x = max(tile_map, key=lambda tile_key: tile_key[0])[0]

    y = max_y
    while y >= min_y:
        print("y =", y, end='')
        if y % 2 == 0:
            print("  ", end='')
        for x in range(min_x, max_x + 1):
            tile = tile_map.get((x, y), None)
            if tile is None:
                col = 'W'
            elif tile.color() == 'black':
                col = 'B'
            else:
                col = 'W'
            # print(" {}({}) ".format(col, x), end='')
            print(" {} ".format(col), end='')
        y -= 1
        print()


def flip_tiles(tile_map):
    new_tile_map = {}

    max_y = max(tile_map, key=lambda tile_key: tile_key[1])[1]
    min_y = min(tile_map, key=lambda tile_key: tile_key[1])[1]
    min_x = min(tile_map, key=lambda tile_key: tile_key[0])[0]
    max_x = max(tile_map, key=lambda tile_key: tile_key[0])[0]
    y = max_y + 1
    while y >= min_y - 1:
        for x in range(min_x - 1, max_x + 2):
            tile = tile_map.get((x, y), Tile())
            tile_pos = (x, y)
            blacks, whites = count_adjacent_black_and_white(tile_pos, tile_map)
            new_tile = Tile()
            # print("Tile in pos {} is {} and has {} black neighbors and {} white neighbors".format(tile_pos, tile.color(), blacks, whites))
            if tile.color() == 'black':
                if blacks == 0 or blacks > 2:
                    # no need to flip, it's white already
                    pass
                else:
                    new_tile.flip()
            else:
                if blacks == 2:
                    new_tile.flip()
            # print("This tile is now:", new_tile.color())
            new_tile_map[tile_pos] = new_tile
        y -= 1

    # for tile_pos in tile_map:
    #     tile = tile_map[tile_pos]
    #     blacks, whites = count_adjacent_black_and_white(tile_pos, tile_map)
    #     new_tile = Tile()
    #     print("Tile in pos {} is {} and has {} black neighbors and {} white neighbors".format(tile_pos, tile.color(), blacks, whites))
    #     if tile.color() == 'black':
    #         if blacks == 0 or blacks > 2:
    #             # no need to flip, it's white already
    #             pass
    #         else:
    #             new_tile.flip()
    #     else:
    #         if blacks == 2:
    #             new_tile.flip()
    #     print("This tile is now:", new_tile.color())
    #     new_tile_map[tile_pos] = new_tile
    return new_tile_map


def solve_part_2(tile_map):
    print("Day 0:", len([tile_id for tile_id in tile_map if tile_map[tile_id].color() == 'black']))
    print_grid(tile_map)
    print()
    for i in range(1):
        new_tile_map = flip_tiles(tile_map)
        print_grid(new_tile_map)
        print()
        tile_map = new_tile_map
        print("Day {}: {}".format((i + 1), len([tile_id for tile_id in tile_map if tile_map[tile_id].color() == 'black'])))
    pass


def solve():
    lines = [line.strip() for line in open("easy.txt").readlines()]
    # lines = [line.strip() for line in open("input.txt").readlines()]
    tile_map = solve_part_1(lines)
    print("Part 1:", len([tile_id for tile_id in tile_map if tile_map[tile_id].color() == 'black']))
    print("Part 2:", solve_part_2(tile_map))


solve()
