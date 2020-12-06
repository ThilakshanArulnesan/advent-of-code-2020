
from utils.read_file import read_file
import re


def has_field(field_name, text):
    found_index = re.search(rf"{field_name}:.*", text)
    return found_index != None


def has_fields(field_name_list, text):
    for field_name in field_name_list:
        if(has_field(field_name, text) == False):
            return False
    return True


def simple_is_passport_valid(text):
    fields_to_check = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        # "cid",
    ]
    return has_fields(fields_to_check, text)


def is_valid_regex(regex, text):
    found_index = re.search(regex, text)
    return found_index != None


def is_invalid_number(number, min, max):
    return int(number) < min or int(number) > max


def validate_passport(text):
    regexes_to_check = [
        r"hcl:#[a-f0-9]{6}\b",
        r"ecl:(amb|blu|brn|gry|grn|hzl|oth)\b",
        r"pid:\d{9}\b"
    ]
    for regex in regexes_to_check:
        if(is_valid_regex(regex, text) == False):
            return False

    # Check birth year
    match = re.search(r'byr:(?P<byr>\d{4})\b', text)
    if(match == None):
        return False
    byr = match.group("byr")

    if(byr == None or is_invalid_number(byr, 1920, 2002)):
        return False

    # Check issue year
    match = re.search(r'iyr:(?P<iyr>\d{4})\b', text)
    if(match == None):
        return False
    iyr = match.group("iyr")

    if(iyr == None or is_invalid_number(iyr, 2010, 2020)):
        return False

    # Check expiration year
    match = re.search(r'eyr:(?P<eyr>\d{4})\b', text)
    if(match == None):
        return False
    eyr = match.group("eyr")
    if(eyr == None or is_invalid_number(eyr, 2020, 2030)):
        return False

    match = re.search(r'hgt:(?P<hgt>\d+)(?P<unit>in|cm)\b', text)
    if(match == None):
        return False
    unit = match.group("unit")
    hgt = match.group("hgt")

    if(unit == "cm" and is_invalid_number(hgt, 150, 193)):
        return False
    if(unit == "in" and is_invalid_number(hgt, 59, 76)):
        return False

    return True


def count_valid_passports(data, withValidation=False):
    num_valid = 0
    next_passport = ""
    passport_num = -1
    for i in range(len(data)):
        line = data[i]
        next_passport = next_passport + " " + line

        # If there is a line break or we've reached the end,
        # the string stored so far is a passport to check
        if(line == "" or i == len(data)-1):
            passport_num += 1
            if(withValidation == False and simple_is_passport_valid(next_passport)):
                num_valid += 1
            elif (validate_passport(next_passport) == True):
                num_valid += 1
            next_passport = ""

    return num_valid


def part1():
    data = read_file('data/d4.in')
    print(f"Number of valid passports: {count_valid_passports(data)}")


def part2():
    data = read_file('data/d4.in')
    print(f"Number of valid passports: {count_valid_passports(data, True)}")
