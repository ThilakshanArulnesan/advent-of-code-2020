import re
from utils.read_file import read_file

def parse_instruction(text):
    match = re.match(r"(?P<instr>nop|acc|jmp) (?P<num>[-+]\d+)", text)
    instr = match.group('instr')
    num = int(match.group('num'))
    return instr, num


def find_acc_val_before_loop(data):
    i = 0
    acc = 0
    visited = set()
    while True:
        if i == len(data):
            return acc, True
        instr, num  = parse_instruction(data[i])

        if i in visited:
            visited.add(i)
            break
        visited.add(i)
        if(instr == "acc"):
            acc += num
            i += 1
        elif(instr == "jmp"):
            i += num
        elif(instr == "nop"):
            i += 1
            
    return acc, False 

def find_acc_with_one_mutation(data):
    i = 0
    while i < len(data):
        if "acc" in  data[i]:
            i += 1
            continue
        new_list = data.copy()
        if "nop" in new_list[i]:
            new_list[i] = new_list[i].replace("nop", "jmp")
            acc, all_visited = find_acc_val_before_loop(new_list)
            if(all_visited):
                return acc
        elif "jmp" in new_list[i]:
            new_list[i] = new_list[i].replace("jmp", "nop")
            acc, all_visited = find_acc_val_before_loop(new_list)
            if(all_visited):
                return acc
        i += 1
    return None

def part1():
    data = read_file('data/d8.in')
    solution, _ = find_acc_val_before_loop(data)
    print(solution)

def part2(): 
    data = read_file('data/d8.in')
    solution = find_acc_with_one_mutation(data)
    print(solution)