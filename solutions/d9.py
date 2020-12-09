from utils.read_file import read_file

def find_num(num_list, preamble_size = 25):
    sum_dict = {}
    for i in range (0, preamble_size):
        for j in range (i+1, preamble_size):
            if(i == j):
                 continue
            sum = num_list[i] + num_list[j]
            sum_dict[sum] = sum_dict[sum] + 1 if sum in sum_dict else 1

    next_pos = preamble_size 

    while(next_pos < len(num_list)):
        num_to_check = num_list[next_pos]
        if(num_to_check not in sum_dict or sum_dict[num_to_check] == 0):
            return num_to_check

        # Remove first digit
        pos_to_remove = next_pos - preamble_size
        for i in range(pos_to_remove+1, pos_to_remove+preamble_size):
            sum_to_remove = num_list[pos_to_remove] + num_list[i]
            sum_dict[sum_to_remove] = sum_dict[sum_to_remove] - 1

        # Add last digit
        for i in range(pos_to_remove+1, next_pos):
            sum = num_to_check + num_list[i]
            sum_dict[sum] = sum_dict[sum] + 1 if sum in sum_dict else 1

        next_pos += 1
    return None   

def find_continguous_list_with_sum(num_list, sum_to_find):
    lower_pointer = 0
    upper_pointer = 1
    sum = num_list[lower_pointer]
    while(True):
        sum  += num_list[upper_pointer]
        if(sum == sum_to_find):
            return num_list[lower_pointer:upper_pointer+1]
        elif(sum > sum_to_find):
            lower_pointer += 1
            upper_pointer = lower_pointer + 1
            sum = num_list[lower_pointer]
        else:
            if(upper_pointer < len(num_list)):
                upper_pointer += 1
            else:
                lower_pointer += 1
                upper_pointer = lower_pointer + 1
                sum = num_list[lower_pointer]

        if(upper_pointer > len(num_list) - 1):
            return None

def sum_min_max(num_list):
    return max(num_list) + min(num_list)


def part1():
    data = read_file('data/d9.in')
    num_list = list(map(lambda x: int(x), data))
    found_num = find_num(num_list)
    print(f"The number that is not the sum of two numbers in the last 25 digits is: {found_num}")

def part2():
    data = read_file('data/d9.in')
    num_list = list(map(lambda x: int(x), data))
    found_num = find_num(num_list)
    contiguous_list = find_continguous_list_with_sum(num_list, found_num)
    print(f"Sum of max and min number in first continguous list that sum to {found_num} is: {sum_min_max(contiguous_list)}")