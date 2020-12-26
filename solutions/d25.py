from utils.read_file import read_file

def apply_operations(value, subject_number = 7, mod = 20201227):
    return (value * subject_number) % mod

def get_loop_size(public_key, subject_number = 7):
    loop_count = 1
    value = subject_number
    while(True):
        loop_count += 1
        value = apply_operations(value, subject_number)
        if(value == public_key):
            return loop_count

def part1():
    data = read_file('data/d25.in')
    card_public_key = int(data[0])
    door_public_key = int(data[1])

    card_loop_size = get_loop_size(card_public_key)
    # door_loop_size = get_loop_size(door_public_key) # Unused, but potentially useful


    subj_num = door_public_key
    for _ in range(0,card_loop_size-1):
        subj_num = apply_operations(subj_num, door_public_key)
    print(f"The encryption key is: {subj_num}")