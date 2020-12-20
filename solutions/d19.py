from utils.read_file import read_file_chunks_no_split

def is_valid(string_to_check, all_rules, rules_to_check):
    if string_to_check == '' or rules_to_check == []:
        return string_to_check == '' and rules_to_check == [] 

    current_rules = all_rules[int(rules_to_check[0])]
    if '"' in current_rules: 
        if string_to_check[0] in current_rules:
            # We've verfied the first character is correct, continue recursively removing the character and the rule
            return is_valid(string_to_check[1:], all_rules, rules_to_check[1:])
        else:
            return False
    else:
        for rule in current_rules:
            # Check all possible rules (since we split them by "|"" ), starting with the left
            # in combination with the remaining rules we need to check 
            if(is_valid(string_to_check,all_rules, rule + rules_to_check[1:])):
                return True
        return False

def part1():
    data = read_file_chunks_no_split('data/d19.in')
    rules_dict = {}
    for rule in data[0].split("\n"):
        rule_num = int(rule.split(": ")[0])
        expr = rule.split(": ")[1]
        if '"' not in expr:
            expr = [t.split() for t in expr.split("|")]
        rules_dict.update({rule_num: expr})
    to_check = data[1].split("\n")

    print(f"Num valid strings: {sum(is_valid(string_to_check,rules_dict,[0]) for string_to_check in to_check)}")    

def part2():
    data = read_file_chunks_no_split('data/d19p2.in')
    rules_dict = {}
    for rule in data[0].split("\n"):
        rule_num = int(rule.split(": ")[0])
        expr = rule.split(": ")[1]
        if '"' not in expr:
            expr = [t.split() for t in expr.split("|")]
        rules_dict.update({rule_num: expr})
    to_check = data[1].split("\n")

    print(f"Num valid strings: {sum(is_valid(string_to_check,rules_dict,[0]) for string_to_check in to_check)}")       
