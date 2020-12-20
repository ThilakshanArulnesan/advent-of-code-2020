from utils.read_file import read_file
import re

def eval_with_add_prio(expr):
    tokens = expr.split(" ")
    tokens_after_sum = []
    tmp = 0

    for token in tokens:
        if(token == "+"):
            continue
        if(token == "*"):
            tokens_after_sum.append(tmp)
            tmp = 0
            continue
        tmp += int(token)
    if(tmp != 0):
        tokens_after_sum.append(tmp)
    prod = 1
    for token in tokens_after_sum:
        prod *= token
    
    return prod
        


def eval(expr, is_part2):
    if(is_part2):
        return eval_with_add_prio(expr)
    
    tokens = expr.split(" ")
    op = "SUM"
    tot = 0
    for token in tokens:
        if(token == "+"):
            op = "SUM"
            continue
        if(token == "*"):
            op = "MULT"
            continue

        if(op == "SUM"):
            tot += int(token)

        if(op == "MULT"):
            tot *= int(token)

    return tot

def solve(line, is_part2 = False):
    if "(" not in line:
        return eval(line, is_part2)
    simplified = ""

    is_open_bracket = False
    open_count = 0
    tmp = ""

    for char in line:
        if char == "(":
            if is_open_bracket:
                tmp += char
            is_open_bracket = True
            open_count += 1
            continue
        if char == ")" and open_count == 1:
            open_count -= 1
            simplified += f"{solve(tmp, is_part2)}"
            is_open_bracket = False
            tmp = ""
            continue
        if char == ")":
            open_count -= 1
        if not is_open_bracket:
            simplified += char
        else:
            tmp += char
    return eval(simplified,is_part2)

def part1():
    data = read_file('data/d18.in')
    val = 0
    for line in data:
        val += solve(line)
    print(f"Sum of solutions: {val}")

def part2():
    data = read_file('data/d18.in')
    val = 0
    for line in data:
        val += solve(line, True)
    print(f"Sum of solutions: {val}")
