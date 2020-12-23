from collections import deque


class CircularList:
    _numbers: deque = []
    _current = -1

    def __init__(self, numbers):
        self._numbers = numbers
        self._current = numbers[0]

    def numbers(self):
        return self._numbers

    def current(self):
        return self._current

    def current_index(self):
        return self._numbers.index(self._current)

    def remove_n_after(self, n, target):
        # Removes the n elements immediately after the target
        target_index = self._numbers.index(target)
        removed = []
        for i in range(n):
            if target_index < len(self._numbers) - 1:
                removed.append(self._numbers.pop(target_index + 1))
            else:
                removed.append(self._numbers.pop(0))
        return removed

    def remove_n_after_current(self, n):
        return self.remove_n_after(n, self.current())

    def insert_after(self, numbers_to_insert, destination):
        # Inserts the n elements immediately after the destination
        destination_index = self._numbers.index(destination)
        for i in range(len(numbers_to_insert)):
            self._numbers.insert(destination_index + i + 1, numbers_to_insert[i])

    def first_smaller_than_current(self):
        # Inserts the n elements immediately after the target
        target = self._numbers[self.current_index()] - 1
        while target not in self._numbers:
            target = target - 1
            if target < 1:
                target = 9
        return target

    def inc_current(self):
        current_index = self._numbers.index(self._current)
        next_index = (current_index + 1) % 9
        self._current = self._numbers[next_index]

    def unroll_from(self, n):
        result = self.remove_n_after(9, n)
        result.remove(n)
        return result


def make_move(circular_list: CircularList):
    next_three = circular_list.remove_n_after_current(3)
    destination = circular_list.first_smaller_than_current()
    circular_list.insert_after(next_three, destination)
    circular_list.inc_current()


def solve_part_1(numbers):
    cups = CircularList(numbers)
    for i in range(100):
        # print("numbers: {}, current: {}".format(cups.numbers(), cups.current()))
        make_move(cups)
    unrolled = cups.unroll_from(1)
    return "".join([str(x) for x in unrolled])


# def solve_part_2(numbers):
#     cups = CircularList(numbers)
#     for i in range(10000000):
#         # print("numbers: {}, current: {}".format(cups.numbers(), cups.current()))
#         make_move(cups)
#     unrolled = cups.unroll_from(1)
#     return "".join([str(x) for x in unrolled])


def solve():
    # data = open('easy.txt', 'r').read()
    numbers = [1, 5, 8, 9, 3, 7, 4, 6, 2]
    # numbers = [3, 8, 9, 1, 2, 5, 4, 6, 7]
    print("Part 1:", solve_part_1(numbers))
    # print("Part 2:", solve_part_2(numbers))


solve()
