from utils.read_file import read_file

def parse(line):
    ingredients, allergens = line.split("(")
    ingredients_list = ingredients.strip().split(" ")
    allergen_list =[a.strip() for a in allergens.split("contains ")[1][0:-1].split(",")]
    return ingredients_list, allergen_list


def part1():
    data = read_file('data/d21.in')
    allergen_dict = {}
    all_ingred = []
    for line in data:
        ingredients_list, allergen_list = parse(line)
        for ing in ingredients_list:
            all_ingred.append(ing)
        for allergen in allergen_list:
            if(allergen in allergen_dict):
                allergen_dict[allergen] = list(set(ingredients_list) & set(allergen_dict[allergen]))
            else:
                allergen_dict.update({allergen: ingredients_list})
    
    potential_allergens = set()

    for allergen in allergen_dict:
        for ing in allergen_dict[allergen]:
            potential_allergens.add(ing)

    good_ing = []
    for ing in all_ingred:
        if(ing not in potential_allergens):
            good_ing.append(ing)
    
    print(f"Number of ingredients that are definitely safe: {len(good_ing)}.")

def part2():
    data = read_file('data/d21.in')
    allergen_dict = {}
    all_ingred = []
    for line in data:
        ingredients_list, allergen_list = parse(line)
        for ing in ingredients_list:
            all_ingred.append(ing)
        for allergen in allergen_list:
            if(allergen in allergen_dict):
                allergen_dict[allergen] = list(set(ingredients_list) & set(allergen_dict[allergen]))
            else:
                allergen_dict.update({allergen: ingredients_list})
    
    queue = []
    for allergen in allergen_dict:
        if(len(allergen_dict[allergen])==1):
            queue.append(allergen_dict[allergen][0])

    while(len(queue) > 0):
        to_remove = queue.pop()
        for allergen in allergen_dict:
            if(to_remove not in allergen_dict[allergen] or len(allergen_dict[allergen]) == 1):
                continue
            allergen_dict[allergen].remove(to_remove)
            if(len(allergen_dict[allergen]) == 1):
                queue.append(allergen_dict[allergen][0])
    sorted_keys = list(allergen_dict.keys())
    sorted_keys.sort()
    
    canonical_dangerous_list = []
    for key in sorted_keys:
        canonical_dangerous_list.append(allergen_dict[key][0])
    canonical_dangerous_string = ",".join(canonical_dangerous_list)
    print(f"The canonical dangerous list is: {canonical_dangerous_string}.")