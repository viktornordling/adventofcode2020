from math import prod


# def eval_tokens(tokens, stack):
#     cur = tokens[0]
#     if cur == '+':
#         left = stack.pop()
#         right = eval_tokens(tokens[1:], stack)
#         stack.push(left + right)
#     elif cur == '*':
#         left = stack.pop()
#         right = eval_tokens(tokens[1:], stack)
#         stack.push(left + right)
#     elif cur == '(':
#         expr
#

def apply_opt(opt, left, right):
    if opt == '+':
        return int(left) + int(right)
    elif opt == '*':
        return int(left) * int(right)


def eval_expr(tokens):
    vals = []
    opts = []
    for t in tokens:
        if t == '':
            continue
        # print("token is ", t)
        if t not in ['*', '+', '(', ')']:
            if len(vals) > 0 and opts[-1] not in ['(', ')']:
                op = opts.pop()
                result = apply_opt(op, vals.pop(), t)
                # print("evaled opt {}, result {}".format(op, result))
                vals.append(result)
            else:
                vals.append(int(t))
        if t in ['(', '+', '*']:
            opts.append(t)
        if t == ')':
            # print("FUCK PARENS!")
            while len(opts) > 0 and len(vals) > 1:
                while opts[-1] == '(':
                    opts.pop()
                result = apply_opt(opts.pop(), vals.pop(), vals.pop())
                # print("evaled paren: ", result)
                vals.append(result)
            if len(opts) > 0 and opts[-1] == '(':
                opts.pop()

    while len(opts) != 0:
        right = vals.pop()
        left = vals.pop()
        result = apply_opt(opts.pop(), left, right)
        vals.append(result)
    print(vals[0])
    return vals[0]


def eval_expr_line(line):
    tokens = [t.strip() for t in line.split(" ")]
    return eval_expr(tokens)


def solve_part_1(lines):
    sum = 0
    for line in lines:
        line = line.replace("(", " ( ")
        line = line.replace(")", " ) ")
        sum += eval_expr_line(line)
    return sum


def solve():
    # lines = open('easy.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()

    print("Part 1:", solve_part_1(lines))
    # print("Part 2:", solve_part_2(lines))


solve()


