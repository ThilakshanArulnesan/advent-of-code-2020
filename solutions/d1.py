from utils.read_file import read_file

def part1():
    def find_nums_sum(list, sum=2020):
        found_nums = set()
        for i in range(len(list)):
            if(list[i] in found_nums):
                return [list[i], sum-list[i]]
            found_nums.add(sum-list[i])

    data = read_file('data/d1.in')
    data_as_int = list(map(lambda x: int(x), data));
    nums_to_multiply = find_nums_sum(data_as_int)

    if nums_to_multiply:
        print(f'Part one solution: {nums_to_multiply[0] * nums_to_multiply[1]}')
    else:
        print("No numbers found with a sum of 2020")

def part2():
    def find_nums_sum(list, sum=2020):
        found_nums = set(list)
        for i in range(len(list)):
            for j in range(i + 1, len(list)):
                if (sum - (list[i] + list[j]) in found_nums):
                     return [list[i],list[j],2020-list[i]-list[j]]

    data = read_file('data/d1.in')
    data_as_int = list(map(lambda x: int(x), data));
    nums_to_multiply = find_nums_sum(data_as_int)

    if nums_to_multiply:
        print(f'Part two solution: {nums_to_multiply[0] * nums_to_multiply[1]}')
    else:
        print("No numbers found with a sum of 2020")
