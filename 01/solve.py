from math import prod


def find_two_numbers_adding_up_to(sum, numbers):
    for number in numbers:
        if (sum - number) in numbers:
            return[number, (sum - number)]


def find_three_numbers_adding_up_to(sum, numbers):
    for number1 in numbers:
        number_to_look_for = sum - number1
        for number2 in numbers:
            if (number_to_look_for - number2) in numbers:
                return[number1, number2, number_to_look_for - number2]


lines = open('input.txt', 'r').readlines()
numbers = set([int(line) for line in lines])
print("Part 1:", prod(find_two_numbers_adding_up_to(2020, numbers)))
print("Part 2:", prod(find_three_numbers_adding_up_to(2020, numbers)))