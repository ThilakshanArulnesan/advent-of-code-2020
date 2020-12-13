from utils.read_file import read_file
import re
import functools 

# ----------PART 1 SOLUTION---------- 

def get_numbers(data):
    return [int(i) for i in re.findall(r'\d+', data[1])]

def get_my_time(data): 
    return int(data[0])

def get_min_waited(number, divisors):
    return [(number // i + 1) * i - number for i in divisors]

def part1():
    data = read_file('data/d13.in')
    
    my_time = get_my_time(data)
    numbers = get_numbers(data)
    min_wait_times = get_min_waited(my_time,numbers)
    
    min_time = min(min_wait_times)
    index_of_min = min_wait_times.index(min_time)
    
    print(f"Product of bus ID by the number of minutes needed to wait: {min_wait_times[index_of_min] * numbers[index_of_min] }")


# ----------PART 2 SOLUTION---------- 
# Idea for part 2:
# Using the example problem with input: 7,13,x,x,59,x,31,19 
# We want a number x, s.t.
#  x % 7 = 0
# (x+1) % 13 = 0
# (x+4) % 59 = 0
# (x + index) % num = 0
# ...
# If we rearrange these equations:
#  x % 7 = 0            => x % 7 = 0
# (x+1) % 13 = 0        => x % 13 = -1 % 13 
# (x+4) % 59 = 0        => x % 59 = -4 % 59 
# (x + index) % num = 0 => x % num = -index % num
# This is now a problem that can be solved using Chinese Remainder Theorem, the idea here is that we can write
# a sum so that each term solves satisfies one of the equations above, while modding to zero for the other terms
# So if our input was just 7,13,x,x,59:
# ANSWER = a * 13 * 59 + b * 7 * 59 + c * 59 * 7
# Where we try all values of a to find a a s.t. a * 13 * 59 = 0 % 7 . 
# We can effectively ignore the other terms because they go to zero mod 7! Using the same idea we
# try all values of b to find a b s.t. b * 7 * 59 = -1 % 13 
# and try all values of c to find a c s.t. c * 59 * 7 = -4 % 59 
# Then we can simplify the answer by taking ANSWER % (7*13*59)

def get_input_list(data):
    return [int(i) if i != 'x' else 'x' for  i in  data.split(",")]

def get_constraints(input_list):
    constraint_list = []
    for i in range(0,len(input_list)):
        if(input_list[i] != 'x'):
            constraint_list.append([input_list[i], i])
    return constraint_list

def find_min_num_for_constraint(num, req_rem,tot_prod):
    start_requirement = tot_prod // num
    for i in range (1, num+1):
        if((start_requirement * i) % num == -req_rem % num):
            return start_requirement * i
    return -1 # should never happen if problem is properly provided

def part2():
    data = read_file('data/d13.in')
    input_list = get_input_list(data[1])
    constraints = get_constraints(input_list)
    modulos = list(map(lambda x: x[0], constraints))
    tot_prod = functools.reduce(lambda a,b : a*b,modulos)

    sums = []
    for constraint in constraints:
        sums.append(find_min_num_for_constraint(constraint[0], constraint[1],tot_prod))
    answer = functools.reduce(lambda a,b : a+b,sums)
    smallest_answer = answer % tot_prod

    print(f"The earliest time that satisfies all the constraints for bus arrivals is: {smallest_answer}")