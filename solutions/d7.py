import re
from utils.read_file import read_file


def parse_text(text, withNum = False):
    matches = re.match(
        r"^(?P<bagtype>\w+ \w+) bags contain", text)
    container = matches.group("bagtype")

    contains_text = text.split("contain")[1]
    contained_bags = []
    bags_text = contains_text.split(",")
    for bag in bags_text:
        if bag == " no other bags.":
            continue
        matches = re.match(
            r" (?P<number>\d+) (?P<bagtype>\w+ \w+) bag", bag)
        number = matches.group("number")
        contained_bag = matches.group("bagtype")
        if(withNum):
            contained_bags.append([int(number),contained_bag])
        else:
            contained_bags.append(contained_bag)

    return container, contained_bags


def find_num_will_contain(bag_dict, bag_type, foundSet):
    sum = 0
    foundSet.add(bag_type)
    to_check = []
    for bag in bag_dict:
        contained_bags = bag_dict[bag]
        if(bag_type in contained_bags and bag not in foundSet):
            foundSet.add(bag)
            to_check.append(bag)
            sum += 1

    for bag in to_check:
        sum += find_num_will_contain(bag_dict, bag, foundSet)

    return sum


def part1():
    bag_dict = {}
    data = read_file("data/d7.in")

    for line in data:
        container, contained_bages = parse_text(line)
        bag_dict[container] = contained_bages

    print(f"Number of bags that can contain \"shiny gold\" within: {find_num_will_contain(bag_dict, 'shiny gold', set(['shiny gold']))}")



def find_total_contained_bags(bag_dict, bag_type):
    sum = 0
    for bags in bag_dict[bag_type]:
        sum += bags[0] + bags[0] *  find_total_contained_bags(bag_dict, bags[1])
    return sum


def part2():
    bag_dict = {}
    data = read_file("data/d7.in")

    for line in data:
        container, contained_bages = parse_text(line, True)
        bag_dict[container] = contained_bages

    total_contained_bags = find_total_contained_bags(bag_dict, 'shiny gold')
    print(f"Number of bags that are within \"shiny gold\": {total_contained_bags}")