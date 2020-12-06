from utils.read_file import read_file_chunks


def num_unique_chars(text):
    found = set()
    for char in text:
        found.add(char)
    return len(found)


def part1():
    groups = read_file_chunks("data/d6.in", "\n\n", "")
    sum = 0
    for group_answers in groups:
        sum += num_unique_chars(group_answers)
    print(f"Sum of unique answers for all groups: {sum}")


def get_num_answered_by_all(group_answers):
    # Can technically be optimized by finding the person who answered the fewest
    characters_to_check = group_answers[0]
    tot = 0

    for character in characters_to_check:
        did_all_answer_yes = True
        for individual_answer in group_answers:
            if(character not in individual_answer):
                did_all_answer_yes = False
                break
        if(did_all_answer_yes):
            tot += 1
    return tot


def part2():
    groups = read_file_chunks("data/d6.in", "\n\n")
    sum = 0
    for group_answers in groups:
        num_answered_by_all = get_num_answered_by_all(group_answers)
        sum += num_answered_by_all

    print(
        f"Sum of questions where all individuals in a group answered \"yes\": {sum}")
