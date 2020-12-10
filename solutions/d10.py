from utils.read_file import read_file

def find_joltage_diff_counts(joltages, initial_joltage = 0):
    counts = [0,0,0,0]
    prev_joltage = 0
    joltages.sort()
    for cur_joltage in joltages:
        diff = cur_joltage - prev_joltage 
        prev_joltage = cur_joltage
        counts[diff] += 1

    return counts



def num_ways(data, num_to_find, memo):
    tot = 0
    for i in range (1,4):
        if num_to_find - i in data:
            if num_to_find - i in memo:
                tot += memo[num_to_find-i]
            else:
                calculated_ways =  num_ways(data, num_to_find - i, memo)
                memo[num_to_find - i] = calculated_ways
                tot += calculated_ways
    return tot

def part1():
    data = list(map(lambda x: int(x), read_file('data/d10.in')))

    # Add the first and last elements
    data.append(0)
    data.append(max(data)+3)

    differences = find_joltage_diff_counts(data)
    print(f"Product of 1 jolt differences with 3 jolt differences: {differences[1] * differences[3]} ")

    
def part2():
    data = list(map(lambda x: int(x), read_file('data/d10.in')))

    # Add the first and last elements
    data.append(0)
    data.append(max(data)+3) # not required as there is only one way to reach this
    data.sort()

    num = num_ways(data, max(data), {0: 1})
    print(f"Number of ways we can add adapters to get to device joltage: {num}")