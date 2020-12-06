from utils.read_file import read_file
import re


def part1():

    def is_valid(min, max, char, text):
        count = 0
        for let in text:
            if(let == char):
                count += 1
        return count <= int(max) and count >= int(min)

    def get_num_valid(list):
        total_valid = 0
        for i in range(len(list)):
            match = re.search(
                r'(?P<min>\d+)-(?P<max>\d+) (?P<char>\w): (?P<text>\w+)', list[i])
            min = match.group("min")
            max = match.group("max")
            char = match.group("char")
            text = match.group("text")
            if is_valid(min, max, char, text):
                total_valid += 1

        return total_valid

    data = read_file('data/d2.in')

    print(f"Number of valid passwords {get_num_valid(data)}")


def part2():

    def is_valid(min, max, char, text):
        pos1 = int(min)-1
        pos2 = int(max)-1

        is_first_position_only = text[pos1] == char and text[pos2] != char
        is_second_position_only = text[pos1] != char and text[pos2] == char

        return is_first_position_only or is_second_position_only

    def get_num_valid(list):
        total_valid = 0
        for i in range(len(list)):
            match = re.search(
                r'(?P<min>\d+)-(?P<max>\d+) (?P<char>\w): (?P<text>\w+)', list[i])
            min = match.group("min")
            max = match.group("max")
            char = match.group("char")
            text = match.group("text")
            if is_valid(min, max, char, text):
                total_valid += 1

        return total_valid

    data = read_file('data/d2.in')
    print(f"Number of valid passwords {get_num_valid(data)}")
