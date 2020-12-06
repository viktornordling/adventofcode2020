from math import prod
import re
import math
import string

def find_yes(group):
    yeses = set()
    for answer in group:
        for letter in answer:
            yeses.add(letter)
    return len(yeses)

def find_all_yes(group):
    all_yes = set([l for l in group[0]])
    for answer in group:
        yeses = set([l for l in answer])
        all_yes = all_yes & yeses
    return len(all_yes)


# lines = open('easy.txt', 'r').read()
lines = open('input.txt', 'r').read()

group_answers = [line.split("\n") for line in lines.split("\n\n")]
# print(group_answers)
num_yeses = [find_yes(group) for group in group_answers]
num_all_yeses = [find_all_yes(group) for group in group_answers]
print(sum(num_yeses))
print(sum(num_all_yeses))