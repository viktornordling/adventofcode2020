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
        if t not in ['*', '+', '(', ')']:
            if len(vals) > 0 and opts[-1] not in ['(', ')']:
                op = opts.pop()
                result = apply_opt(op, vals.pop(), t)
                vals.append(result)
            else:
                vals.append(int(t))
        if t in ['(', '+', '*']:
            opts.append(t)
        if t == ')':
            if opts[-1] == '(':
                opts.pop()
            while len(opts) > 0 and opts[-1] != '(':
                result = apply_opt(opts.pop(), vals.pop(), vals.pop())
                vals.append(result)

    while len(opts) != 0:
        right = vals.pop()
        left = vals.pop()
        result = apply_opt(opts.pop(), left, right)
        vals.append(result)
    return vals[0]


def eval_expr_2(tokens):
    vals = []
    opts = []
    for t in tokens:
        if t == '':
            continue
        if t not in ['*', '+', '(', ')']:
            vals.append(int(t))
        if t in ['(', '+', '*']:
            while len(opts) > 0 and opts[-1] == '+' and t == '*':
                result = apply_opt(opts.pop(), vals.pop(), vals.pop())
                vals.append(result)
            opts.append(t)
        if t == ')':
            if opts[-1] == '(':
                opts.pop()
            while len(opts) > 0 and opts[-1] != '(':
                result = apply_opt(opts.pop(), vals.pop(), vals.pop())
                vals.append(result)
            if opts[-1] == '(':
                opts.pop()

    while len(opts) != 0:
        right = vals.pop()
        left = vals.pop()
        result = apply_opt(opts.pop(), left, right)
        vals.append(result)
    return vals[0]


def eval_expr_line(line):
    tokens = [t.strip() for t in line.split(" ")]
    return eval_expr(tokens)


def eval_expr_line_2(line):
    tokens = [t.strip() for t in line.split(" ")]
    return eval_expr_2(tokens)


def solve_part_1(lines):
    sum = 0
    for line in lines:
        line = line.replace("(", " ( ")
        line = line.replace(")", " ) ")
        sum += eval_expr_line(line)
    return sum


def solve_part_2(lines):
    sum = 0
    for line in lines:
        line = line.replace("(", " ( ")
        line = line.replace(")", " ) ")
        sum += eval_expr_line_2(line)
    return sum


def solve():
    # lines = open('easy.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()

    print("Part 1:", solve_part_1(lines))
    print("Part 2:", solve_part_2(lines))


solve()

