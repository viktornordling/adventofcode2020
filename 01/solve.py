from math import prod


def find_two_numbers_adding_up_to(sum, numbers):
    for number in numbers:
        if (sum - number) in numbers:
            return[number, (sum - number)]
    return None


def find_three_numbers_adding_up_to(sum, numbers):
    for number1 in numbers:
        number_to_look_for = sum - number1
        found = find_two_numbers_adding_up_to(number_to_look_for, numbers)
        if found is not None:
            return found + [number1]


lines = open('input.txt', 'r').readlines()
numbers = set([int(line) for line in lines])
print("Part 1:", prod(find_two_numbers_adding_up_to(2020, numbers)))
print("Part 2:", prod(find_three_numbers_adding_up_to(2020, numbers)))