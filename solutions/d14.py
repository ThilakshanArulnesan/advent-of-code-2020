from utils.read_file import read_file
import re

def get_masks(string):
    mask_1 = string.replace('1', '0').replace('X','1')
    mask_2 = string.replace('X','0')
    return int(mask_1,2), int(mask_2,2)

def apply_masks(num, and_mask, or_mask):
    return (num & and_mask) | or_mask


def part1():
    data = read_file('data/d14.in')
    stored_dict = {}

    for line in data:
        if("mask" in line):
            and_mask, or_mask  = get_masks(line.split("= ")[1])
        else:
            # mem[8] = 11
            match = re.match(r"mem\[(?P<loc>\d+)\] = (?P<num>\d+)",line)
            loc = int(match.group("loc"))
            num = int(match.group("num"))
            stored_dict[loc] = apply_masks(num,and_mask,or_mask)

    print(f"Sum of stored values after all instructions completed: {sum(stored_dict.values())}")

def update_dict(stored_dict, inst, mask):
    loc, num = inst
    
    # Fix the 1 bits:
    b1 = mask.replace("X", "0")
    with_1bits = loc | int(b1,2) # Adds one to all locations where there is a 1

    # Clears out all the bits positioned at X's as they will be replaced
    b2 = mask.replace("0","1").replace("X", "0")
    mask_without_x = with_1bits & int(b2,2) 

    mask_for_x = mask.replace("1","0") # Zero all digits except the X which we will do a bitwise OR with
    num_x = mask.count("X")
    for i in range (0, 2**num_x):
        x = i
        # Systematic way of replacing X's with all possible combinations of 0 and 1
        while("X" in mask_for_x):
            mask_for_x = mask_for_x.replace("X", f"{x % 2}",1)
            x = x // 2
        actual_loc = mask_without_x | int(mask_for_x,2)
        
        # Avoid writing to the same memory address
        if(not actual_loc in stored_dict):
            stored_dict[actual_loc] = num

        mask_for_x = mask.replace("1","0") # Reset the mask for the next possible combination

def part2():
    data = read_file('data/d14.in')

    stored_dict = {}
    inst_list = []
    # Go through data in reverse, we don't care about the any values that would have gotten re-written
    # So the ones at the bottom take precedence
    for i in range (len(data), 0, -1):
        line = data[i-1]
        if("mask" in line):
            mask = line.split("= ")[1]
            for inst in inst_list:
                update_dict(stored_dict, inst, mask)
            inst_list=[]
        else:
            match = re.match(r"mem\[(?P<loc>\d+)\] = (?P<num>\d+)",line)
            loc = int(match.group("loc"))
            num = int(match.group("num"))
            inst_list.append([loc,num])
        if(len(stored_dict) == 2**36):
            break
    print(f"Sum of stored values after all instructions completed: {sum(stored_dict.values())}")
