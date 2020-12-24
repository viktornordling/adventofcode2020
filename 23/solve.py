from collections import deque


class Element:
    def __init__(self, value):
        self._value = value
        self._nxt = None
        self._prev = None

    def set_next(self, nxt):
        self._nxt = nxt

    def set_prev(self, prev):
        self._prev = prev

    def next(self):
        return self._nxt

    def prev(self):
        return self._prev


class CircularLinkedList:
    _current: Element

    def __init__(self, value):
        self._current = Element(value)

    def add(self, value):
        nxt = Element(value)
        nxt.set_prev(self._current)

        org_next = self._current.next()
        if org_next is not None:
            org_next.set_prev(nxt)

        self._current.set_next(nxt)
        self._current = nxt

    def remove(self, value):
        removed = Element(value)
        nxt.set_prev(self._current)


        self._current.set_next(nxt)
        self._current = nxt


class CircularList:
    _numbers: deque = []
    # _current = -1
    _current_index = -1
    _max = -1

    def __init__(self, numbers):
        self._numbers = numbers
        # self._current = numbers[0]
        self._current_index = 0
        self._max = max(numbers)

    def numbers(self):
        return self._numbers

    def current_index(self):
        return self._current_index

    def remove_n_after_index(self, n, target_index):
        # Removes the n elements immediately after the target
        removed = []
        for i in range(n):
            if target_index < len(self._numbers) - 1:
                removed.append(self._numbers.pop(target_index + 1))
            else:
                removed.append(self._numbers.pop(0))
        return removed

    def remove_n_after_current(self, n):
        return self.remove_n_after_index(n, self._current_index)

    def insert_after(self, numbers_to_insert, destination):
        # Inserts the n elements immediately after the destination
        destination_index = self._numbers.index(destination)
        for i in range(len(numbers_to_insert)):
            self._numbers.insert(destination_index + i + 1, numbers_to_insert[i])

    def first_smaller_than_current(self):
        target = self._numbers[self.current_index()] - 1
        while target not in self._numbers:
            target = target - 1
            if target < 1:
                target = self._max
        return target

    def inc_current_index(self):
        self._current_index = (self._current_index + 1) % len(self._numbers)

    def unroll_from(self, n):
        result = self.remove_n_after_index(9, self._numbers.index(n))
        result.remove(n)
        return result

    def next_n_after(self, n, element):
        index = self._numbers.index(element)
        return [self._numbers[i % len(self._numbers)] for i in range(index, index + n)]


def make_move(circular_list: CircularList):
    next_three = circular_list.remove_n_after_current(3)
    destination = circular_list.first_smaller_than_current()
    circular_list.insert_after(next_three, destination)
    circular_list.inc_current_index()


def solve_part_1():
    numbers = [1, 5, 8, 9, 3, 7, 4, 6, 2]
    cups = CircularList(numbers)
    for i in range(100):
        print("numbers: {}, current: {}".format(cups.numbers(), cups.current_index()))
        make_move(cups)
    unrolled = cups.unroll_from(1)
    return "".join([str(x) for x in unrolled])


def solve_part_2():
    # linked_list = deque([1, 5, 8, 9, 3, 7, 4, 6, 2])
    linked_list = deque([3, 8, 9, 1, 2, 5, 4, 6, 7])
    for i in range(10, 1000001):
        linked_list.append(i)
    print(len(linked_list))
    cups = CircularList(linked_list)
    for i in range(10000000):
        # print("numbers: {}, current: {}".format(cups.numbers(), cups.current()))
        make_move(cups)
    a, b = cups.next_n_after(2, 1)
    return a * b


def solve():
    print("Part 1:", solve_part_1())
    # print("Part 2:", solve_part_2(numbers))


solve()
