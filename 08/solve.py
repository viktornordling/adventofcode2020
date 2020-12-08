from math import prod
import re
import math
import string

def parse(line):
    parts = line.split(" ")
    return {'op': parts[0], 'arg': int(parts[1])}


ops = {
    'nop': lambda op, acc, arg: (op + 1, acc),
    'acc': lambda op, acc, arg: (op + 1, acc + arg),
    'jmp': lambda op, acc, arg: (op + arg, acc),
}

# lines = open('easy.txt', 'r').readlines()
lines = open('input.txt', 'r').readlines()
program = [parse(line) for line in lines]

line_number = 0
acc = 0
seen_instrs = set()
while True:
    if line_number in seen_instrs:
        print("Part 1:", acc)
        break
    line = program[line_number]
    op = ops[line['op']]
    seen_instrs.add(line_number)
    line_number, acc = op(line_number, acc, line['arg'])

nop_lines = [line_number for line_number, line in enumerate(program) if line['op'] == 'nop']
jmp_lines = [line_number for line_number, line in enumerate(program) if line['op'] == 'jmp']

for jmp_line in jmp_lines:
    line_number = 0
    acc = 0
    seen_instrs = set()
    while True:
        if line_number in seen_instrs:
            break
        if line_number >= len(program):
            print("Part 2:", acc)
            break
        line = program[line_number]
        op = ops[line['op']]
        if (line_number == jmp_line):
            op = ops['nop']
        seen_instrs.add(line_number)
        line_number, acc = op(line_number, acc, line['arg'])

for nop_line in nop_lines:
    line_number = 0
    acc = 0
    seen_instrs = set()
    while True:
        if line_number in seen_instrs:
            break
        if line_number >= len(program):
            print("Part 2:", acc)
            break
        line = program[line_number]
        op = ops[line['op']]
        if (line_number == nop_line):
            op = ops['jmp']
        seen_instrs.add(line_number)
        line_number, acc = op(line_number, acc, line['arg'])
