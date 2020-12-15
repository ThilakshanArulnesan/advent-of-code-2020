


def find_num_spoken(initial_dict, last_number, num_to_find):
    #Map 
    last_known_dict = initial_dict

    last_number = 6
    min_range = len(last_known_dict) + 1
    for i in range (min_range, num_to_find):
        next_num = 0
        if(last_number in last_known_dict):
            next_num = (i-1) - last_known_dict[last_number]
        last_known_dict[last_number] = i-1
        last_number = next_num
    return next_num

def part1():
    initial_dict = {
        2: 1,
        1: 2,
        10: 3,
        11: 4,
        0: 5,
        6: 6
    }
    answer = find_num_spoken(initial_dict, 6, 2021)
    print(f"The number spoken at step 2020 is {answer}")

def part2():
    initial_dict = {
        2: 1,
        1: 2,
        10: 3,
        11: 4,
        0: 5,
        6: 6
    }
    answer = find_num_spoken(initial_dict, 6, 30000001)
    print(f"The number spoken at step 30000000 is {answer}")