from utils.read_file import read_file_chunks_no_split
import re

def parse_rule(rule):
    match = re.match(r"(?P<name>.*): (?P<num1>\d+)-(?P<num2>\d+) or (?P<num3>\d+)-(?P<num4>\d+)", rule)
    name = match.group("name")
    num1 = int(match.group("num1"))
    num2 = int(match.group("num2"))
    num3 = int(match.group("num3"))
    num4 = int(match.group("num4"))
    return name, num1, num2, num3, num4

def is_valid_number(number, rules_list):
    for rule in rules_list:
        is_invalid = ((number < rule[0][0] or number > rule[0][1])
            and (number < rule[1][0] or number > rule[1][1]))
        if(not is_invalid):
             return 0
    return number

def valid_rules(number, rules_list):
    valid_rules_set = set()
    for rule in rules_list:
        is_invalid = ((number < rule[0][0] or number > rule[0][1])
            and (number < rule[1][0] or number > rule[1][1]))
        
        if(not is_invalid):
            valid_rules_set.add(rule[2])
    return valid_rules_set

def part1():
    data = read_file_chunks_no_split('data/d16.in')

    unparsed_rules = data[0].split("\n")
    rules_list = []
    for rule in unparsed_rules:
        _, n1,n2,n3,n4 = parse_rule(rule)
        rules_list.append([[n1,n2], [n3,n4]])
        
    tickets = data[2].split("\n")[1:]

    scanning_error_rate = 0
    for ticket in tickets:
        numbers = list(map(lambda x : int(x), ticket.split(",")))
        scanning_error_rate += sum([is_valid_number(num, rules_list) for num in numbers])
    print(f"Scanning error rate: {scanning_error_rate}")

def simplify_set(set_list, rule_list):
    rule_names = [r[2] for r in rule_list]
    while(sum([len(l) for l in set_list]) != len(set_list)):
        rules_to_find = []

        # Find any rules that only appear in one position
        for rule_name in rule_names:
            count = 0
            for i in range(0,len(set_list)):
                options = set_list[i]
                if(rule_name in options):
                    count+=1
            if(count ==1):
                rules_to_find.append(rule_name)

        for i in range(0,len(set_list)):
            options = set_list[i]

            # Check if there is only one rule that applies, remove that rule from all other sets
            if(len(options) == 1):
                set_list = [s.difference(options) for s in set_list]
                set_list[i] = options
            # Check if the rule is one of the ones that appears in only this position
            for rule in rules_to_find:
                if(rule in options):
                    set_list[i] = set()
                    set_list[i].add(rule)
    return set_list

def part2():
    data = read_file_chunks_no_split('data/d16.in')

    unparsed_rules = data[0].split("\n")
    rules_list = []
    for rule in unparsed_rules:
        name, n1,n2,n3,n4 = parse_rule(rule)
        rules_list.append([[n1,n2], [n3,n4], name])
        
    tickets = data[2].split("\n")[1:]
    valid_tickets = []

    for ticket in tickets:
        numbers = list(map(lambda x : int(x), ticket.split(",")))
        count_invalid =  sum([is_valid_number(num, rules_list) for num in numbers])
        if(count_invalid == 0):
            valid_tickets.append(numbers)
 
    set_list = []
    for i in range(0,len(valid_tickets[0])):
        set_list.append( valid_rules(valid_tickets[0][i], rules_list))
        for j in range(1,len(valid_tickets)):
            valid_ticket = valid_tickets[j]
            set_list[i] = set_list[i] & valid_rules(valid_ticket[i], rules_list)
    
    uniq_set = simplify_set(set_list,rules_list)
    
    positions_to_multiply = []
    for i, rule_name in enumerate(uniq_set): 
        if('departure' in "".join(list(rule_name))):
            positions_to_multiply.append(i)
    my_numbers = list(map(lambda x: int(x),data[1].split("\n")[1:][0].split(",")))

    prod = 1
    for pos in positions_to_multiply:
        prod *= my_numbers[pos]

    print(f"Product of numbers in fields starting with departure: {prod}")