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

    def value(self):
        return self._value


class CircularLinkedList:
    _current: Element
    _val_to_element: {}

    def __init__(self, value):
        self._current = Element(value)
        self._current.set_next(self._current)
        self._current.set_prev(self._current)
        self._val_to_element = {value: self._current}

    def get_current(self):
        return self._current

    def set_current(self, element):
        self._current = element

    def add(self, value):
        nxt = Element(value)
        nxt.set_prev(self._current)

        org_next = self._current.next()
        if org_next is not None:
            nxt.set_next(org_next)
            org_next.set_prev(nxt)

        self._current.set_next(nxt)
        self._current = nxt

        self._val_to_element[value] = nxt

    def remove_next(self):
        to_remove = self._current.next()
        self._current.set_next(to_remove.next())
        to_remove.next().set_prev(self._current)
        self._val_to_element.pop(to_remove.value())
        return to_remove.value()

    def remove_n_after_current(self, n):
        return [self.remove_next() for _ in range(n)]

    def first_smaller_than_current(self):
        target = self._current.value() - 1
        while target not in self._val_to_element:
            target = target - 1
            if target < 1:
                target = max(self._val_to_element)
        return target

    def unroll_from(self, value):
        start = self._val_to_element[value]
        start_value = start.value()
        unrolled = []
        while True:
            unrolled.append(start.value())
            start = start.next()
            if start.value() == start_value:
                break
        return unrolled[1:]

    def unroll(self):
        start = self._current
        start_value = start.value()
        unrolled = []
        while True:
            unrolled.append(start.value())
            start = start.next()
            if start.value() == start_value:
                break
        return unrolled[1:]

    def insert_after(self, destination_value, values_to_insert):
        org_current = self._current
        element = self._val_to_element[destination_value]
        self._current = element
        for value in values_to_insert:
            self.add(value)
        self._current = org_current

    def move_current_to_next(self):
        self._current = self._current.next()

    def next_n_after(self, n, value):
        current = self._val_to_element[value]
        result = []
        for _ in range(n):
            current = current.next()
            result.append(current.value())
        return result


def make_move(circular_list: CircularLinkedList):
    next_three = circular_list.remove_n_after_current(3)
    # print("Pick up:", next_three)
    destination = circular_list.first_smaller_than_current()
    # print("Destination:", destination)
    circular_list.insert_after(destination, next_three)
    circular_list.move_current_to_next()


def solve_part_1():
    # numbers = [3, 8, 9, 1, 2, 5, 4, 6, 7]
    numbers = [1, 5, 8, 9, 3, 7, 4, 6, 2]
    cups = CircularLinkedList(numbers.pop(0))
    current = cups.get_current()
    for value in numbers:
        cups.add(value)
    cups.set_current(current)
    for i in range(100):
        make_move(cups)
    unrolled = cups.unroll_from(1)
    return "".join([str(x) for x in unrolled])


def solve_part_2():
    # numbers = [3, 8, 9, 1, 2, 5, 4, 6, 7]
    numbers = [1, 5, 8, 9, 3, 7, 4, 6, 2]
    for i in range(10, 1000001):
        numbers.append(i)
    cups = CircularLinkedList(numbers.pop(0))
    current = cups.get_current()
    for value in numbers:
        cups.add(value)
    cups.set_current(current)
    for i in range(10000000):
        make_move(cups)
    a, b = cups.next_n_after(2, 1)
    return a * b


def solve():
    print("Part 1:", solve_part_1())
    print("Part 2:", solve_part_2())


solve()
