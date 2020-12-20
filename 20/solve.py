import math
from collections import deque


class Piece:
    id = 0
    sides = []
    piece = []

    def __init__(self, id, sides, full_piece):
        self.id = id
        self.sides = deque(sides)
        self.full_piece = full_piece

    def full_minus_frame(self):
        new = []
        for arr in self.full_piece[1:-1]:
            newarr = []
            for a in arr[1:-1]:
                newarr.append(a)
            new.append(newarr)
        return new

    def rotate(self):
        top = self.sides[0]
        right = self.sides[1]
        bottom = self.sides[2]
        left = self.sides[3]
        self.sides[0] = left[::-1]
        self.sides[1] = top
        self.sides[2] = right[::-1]
        self.sides[3] = bottom

        width = len(self.full_piece[0])
        new = []
        for arr in self.full_piece:
            newarr = []
            for a in arr:
                newarr.append(a)
            new.append(newarr)
        for y in range(width):
            for x in range(width):
                new_x = width - y - 1
                new_y = x
                new[new_y][new_x] = self.full_piece[y][x]
        self.full_piece = new

    def flip(self):
        top = self.sides[0]
        right = self.sides[1]
        bottom = self.sides[2]
        left = self.sides[3]
        top = top[::-1]
        bottom = bottom[::-1]
        self.sides[0] = top
        self.sides[1] = left
        self.sides[2] = bottom
        self.sides[3] = right

        width = len(self.full_piece[0])
        new = []
        for arr in self.full_piece:
            newarr = []
            for a in arr:
                newarr.append(a)
            new.append(newarr)
        for y in range(width):
            for x in range(width):
                new_x = width - x - 1
                new_y = y
                new[new_y][new_x] = self.full_piece[y][x]
        self.full_piece = new


def pieces_fit(a: Piece, b: Piece):
    for s1 in a.sides:
        for s2 in b.sides:
            if s1 == s2 or s1 == s2[::-1]:
                return True
    return False


# Check if b can fit to the right of a, allowing b to be rotated and flipped, but not a.
def b_fits_on_right_of_a(a: Piece, b: Piece):
    right = a.sides[1]
    for s2 in b.sides:
        if right == s2 or right == s2[::-1]:
            return True
    return False


# Check if b fits to the right of a, allowing none of the pieces to be rotated
def b_fits_on_right_of_a_no_rot(a: Piece, b: Piece):
    a_right = a.sides[1]
    b_left = b.sides[3]
    return a_right == b_left


def b_fits_below_of_a_no_rot(a: Piece, b: Piece):
    a_bottom = a.sides[2]
    b_top = b.sides[0]
    return a_bottom == b_top

        
# Check if b can fit below a, allowing b to be rotated and flipped, but not a.
def b_fits_below_a(a: Piece, b: Piece):
    bottom = a.sides[2]
    for s2 in b.sides:
        if bottom == s2 or bottom == s2[::-1]:
            return True
    return False


def find_fit(fit_map, cur_piece, used_pieces):
    # find each piece which fits with the one on its left, and rotate / flip it into place
    fits = fit_map[cur_piece]
    for p in fits:
        if p in used_pieces:
            continue
        for j in range(9):
            if b_fits_on_right_of_a_no_rot(cur_piece, p):
                # found the fitting piece, put it in!
                return p
            if j == 4:
                p.flip()
            else:
                p.rotate()
    raise Exception("Found no fit")


def find_fit_below(fit_map, cur_piece, used_pieces):
    # find each piece which fits with the one on its left, and rotate / flip it into place
    fits = fit_map[cur_piece]
    for p in fits:
        if p in used_pieces:
            continue
        for j in range(9):
            if b_fits_below_of_a_no_rot(cur_piece, p):
                # found the fitting piece, put it in!
                return p
            if j == 4:
                p.flip()
            else:
                p.rotate()
    raise Exception("Found no fit")


def flip_grid(grid):
    width = len(grid[0])
    height = len(grid)
    new = []
    for arr in grid:
        newarr = []
        for a in arr:
            newarr.append(a)
        new.append(newarr)
    for y in range(height):
        for x in range(width):
            new_x = width - x - 1
            new_y = y
            new[new_y][new_x] = grid[y][x]
    return new


def rotate_grid(grid):
    width = len(grid[0])
    height = len(grid)
    new = []
    for arr in grid:
        newarr = []
        for a in arr:
            newarr.append(a)
        new.append(newarr)
    for y in range(height):
        for x in range(width):
            new_x = width - y - 1
            new_y = x
            new[new_y][new_x] = grid[y][x]
    return new


def solve_row(row_number, first_piece, fits, puzzle, puzzle_width, used_pieces):
    cur_piece = first_piece
    for i in range(puzzle_width - 1):
        p = find_fit(fits, cur_piece, used_pieces)
        used_pieces.add(p)
        puzzle[(i + 1, row_number)] = p
        cur_piece = p


def mask_matches(start_x, start_y, grid, mask):
    mask_width = len(mask[0])
    mask_height = len(mask)
    for y in range(mask_height):
        for x in range(mask_width):
            mask_char = mask[y][x]
            if mask_char == '#' and grid[start_y + y][start_x + x] != '#':
                return False
    return True


def mark_match(start_x, start_y, grid, mask):
    mask_width = len(mask[0])
    mask_height = len(mask)
    for y in range(mask_height):
        for x in range(mask_width):
            mask_char = mask[y][x]
            if mask_char == '#':
                grid[start_y + y][start_x + x] = 'O'


def find_and_mark_monsters(grid, mask):
    width = len(grid[0])
    height = len(grid)
    mask_width = len(mask[0])
    mask_height = len(mask)
    for y in range(height - mask_height - 1):
        for x in range(width - mask_width - 1):
            if mask_matches(x, y, grid, mask):
                mark_match(x, y, grid, mask)


def solve_part_1_and_2(data, mask):
    pieces = data.split("\n\n")
    parsed_pieces = []
    for piece in pieces:
        lines = piece.split("\n")
        idline = lines[0]
        id = idline.split(" ")[1]
        id = id.replace(":", "")
        top = lines[1]
        bottom = lines[-1]
        left = "".join([line[0] for line in lines[1:]])
        right = "".join([line[-1] for line in lines[1:]])
        full_piece = []
        for line in lines[1:]:
            full_piece.append([x for x in line])
        parsed_pieces.append(Piece(id, [top, right, bottom, left], full_piece))

    piece_to_fitting_map = {}

    for piece1 in parsed_pieces:
        for piece2 in parsed_pieces:
            if piece1.id != piece2.id:
                if pieces_fit(piece1, piece2):
                    cur = piece_to_fitting_map.get(piece1, [])
                    cur.append(piece2)
                    piece_to_fitting_map[piece1] = cur

    corners = []
    for piece in piece_to_fitting_map:
        if len(piece_to_fitting_map[piece]) == 2:
            corners.append(piece)

    corner_ids = [int(corner.id.replace(":", "")) for corner in corners]
    print("Part 1:", math.prod(corner_ids))

    # Strategy: take one of the corner pieces and put it in a corner (any corner is fine since we can just
    # rotate the puzzle. Say top left corner. Now keep building to the right.
    # top_left = corners.pop()
    #
    # rotate the piece so that it has the sides that fit with other pieces as the right and bottom sides
    # get the two pieces that fit with this corner piece
    top_left = corners[0]
    two_fitting = piece_to_fitting_map[top_left]
    # rotate / flip the top left piece so two pieces fit
    both_fit = False
    for i in range(9):
        if both_fit:
            break
        a = two_fitting[0]
        b = two_fitting[1]
        a_fits = False
        b_fits = False
        if b_fits_on_right_of_a(top_left, a):
            a_fits = True
        if b_fits_below_a(top_left, b):
            b_fits = True
        if a_fits and b_fits:
            both_fit = True
        else:
            if i == 4:
                top_left.flip()
            else:
                top_left.rotate()

    puzzle = {(0, 0): top_left}
    puzzle_width = int(math.sqrt(len(parsed_pieces)))
    used_pieces = set()
    used_pieces.add(top_left)
    first = top_left

    # solve all rows
    for i in range(puzzle_width):
        solve_row(i, first, piece_to_fitting_map, puzzle, puzzle_width, used_pieces)
        # for each new row, find the first piece for the next row
        if i < puzzle_width - 1:
            first = find_fit_below(piece_to_fitting_map, puzzle[(0, i)], used_pieces)
            used_pieces.add(first)
            puzzle[(0, i + 1)] = first
    big_puzzle = []
    puzzle_side_width = len(top_left.full_piece[0])

    for y in range(puzzle_width):
        for _ in range(puzzle_side_width - 2):
            big_puzzle.append(['.' for _ in range(puzzle_width * (puzzle_side_width - 2))])
        for x in range(puzzle_width):
            piece = puzzle[(x, y)]
            full = piece.full_minus_frame()
            pw = len(full[0])
            for a in range(pw):
                for b in range(pw):
                    big_y = y * pw + a
                    big_x = x * pw + b
                    grr = full[a][b]
                    big_puzzle[big_y][big_x] = grr

    for i in range(9):
        find_and_mark_monsters(big_puzzle, mask)
        if i == 4:
            big_puzzle = flip_grid(big_puzzle)
        else:
            big_puzzle = rotate_grid(big_puzzle)
    print("Part 2:", count_hashes(big_puzzle))


def count_hashes(big_puzzle):
    count = 0
    big_width = len(big_puzzle[0])
    for y in range(0, big_width):
        for x in range(0, big_width):
            if big_puzzle[y][x] == '#':
                count += 1
    return count


def print_big_puzzle(big_puzzle):
    big_width = len(big_puzzle[0])
    for y in range(0, big_width):
        for x in range(0, big_width):
            print(big_puzzle[y][x], end='')
        print()


def solve():
    mask = [line.replace("\n", "") for line in open('mask.txt', 'r').readlines()]
    data = open('input.txt', 'r').read()
    solve_part_1_and_2(data, mask)


solve()
