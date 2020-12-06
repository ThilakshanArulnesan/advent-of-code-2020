from utils.read_file import read_file


def BF_convert_to_binary_string(str):
    return (str.replace("F", "0").replace("B", "1"))


def RL_convert_to_binary_string(str):
    return (str.replace("L", "0").replace("R", "1"))


def return_base_10(num):
    return int(num, 2)


def get_seat_id(string):
    binary_seat_row = BF_convert_to_binary_string(string[0:7])
    seat_row = return_base_10(binary_seat_row)

    binary_seat_column = RL_convert_to_binary_string(string[-3:])
    seat_column = return_base_10(binary_seat_column)

    return seat_row * 8 + seat_column


def part1():
    data = read_file('data/d5.in')
    max_num = -1
    for line in data:
        seat_id = get_seat_id(line)
        if(seat_id > max_num):
            max_num = seat_id
    print(max_num)


def find_my_seat(valid_seats):
    for i in range(len(valid_seats)):
        seat_id = valid_seats[i]
        if seat_id+1 not in valid_seats and seat_id-1 not in valid_seats:
            return seat_id


def part2():
    MIN_SEAT = 8  # Can't be very back, so 0-7 not possible
    MAX_SEAT = 1015  # Can't be very front, so MAX = 126 * 8 + 7
    valid_seats = list(range(MIN_SEAT, MAX_SEAT+1))
    valid_seats.remove(8)

    data = read_file('data/d5.in')
    for line in data:
        seat_id = get_seat_id(line)
        valid_seats.remove(seat_id)

    print(find_my_seat(valid_seats))
