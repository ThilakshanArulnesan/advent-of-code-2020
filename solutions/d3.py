
from utils.read_file import read_file


def is_tree(char):
    return char == "#"


def find_num_trees(data, down=1, right=3):
    width = len(data[0])
    num_to_check = 0
    total_trees = 0

    for i in range(0, len(data), down):
        line = data[i]
        # if()
        if(is_tree(line[num_to_check])):
            total_trees += 1
        num_to_check = (num_to_check + right) % width

    return total_trees


def part1():
    data = read_file('data/d3.in')
    num_trees = find_num_trees(data, 1, 3)
    print(f"Number of trees collided with: {num_trees}")


def part2():
    data = read_file('data/d3.in')
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]
    answer = 1
    for slope in slopes:
        answer *= find_num_trees(data, slope[1], slope[0])

    print(
        f"Product of number of trees collided with for all given slopes: {answer}")
