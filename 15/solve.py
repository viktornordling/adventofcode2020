def print_i_th_number(i):
    last_said = {}
    # startings = [0, 3, 6]
    startings = [16, 1, 0, 18, 12, 14, 19]
    next_number_to_speak = 0
    for turn in range(i):
        if (turn + 1) % 1000000 == 0:
            print("Turn is", turn + 1)
        if turn < len(startings):
            last = startings[turn]
            last_said[last] = turn
        else:
            number_to_speak = next_number_to_speak
            if turn == (i - 1):
                return number_to_speak
            if last_said.get(next_number_to_speak, None) is not None:
                next_number_to_speak = turn - last_said[number_to_speak]
            else:
                next_number_to_speak = 0
            last_said[number_to_speak] = turn


def solve():
    print("Part 1:", print_i_th_number(2020))
    print("Part 2:", print_i_th_number(30_000_000))


solve()


