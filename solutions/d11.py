from utils.read_file import read_file

def is_occupied_seat(char):
    return char == '#'
def is_empty_seat(char):
    return char == 'L'
def is_floor(char):
    return char == '.'

def line_of_sight_seat_occupied(seat_matrix, row, column, vec, is_line_of_sight):
    num_rows = len(seat_matrix)
    num_columns = len(seat_matrix[0])

    row += vec[0]
    column += vec[1]

    while(row >=0 and row < num_rows and column >=0 and column < num_columns):
        if(is_occupied_seat(seat_matrix[row][column])):
            return 1
        if(is_empty_seat(seat_matrix[row][column])):
            return 0
        if(not is_line_of_sight): 
            return 0
        row += vec[0]
        column += vec[1]
    return 0

def num_neighbors(seat_matrix, row, column, is_line_of_sight):
    count = 0
    count += line_of_sight_seat_occupied(seat_matrix, row, column, [1,0], is_line_of_sight)
    count += line_of_sight_seat_occupied(seat_matrix, row, column, [1,1], is_line_of_sight)
    count += line_of_sight_seat_occupied(seat_matrix, row, column, [1,-1], is_line_of_sight)
    count += line_of_sight_seat_occupied(seat_matrix, row, column, [-1,0], is_line_of_sight)
    count += line_of_sight_seat_occupied(seat_matrix, row, column, [-1,1], is_line_of_sight)
    count += line_of_sight_seat_occupied(seat_matrix, row, column, [-1,-1], is_line_of_sight)
    count += line_of_sight_seat_occupied(seat_matrix, row, column, [0,1], is_line_of_sight)
    count += line_of_sight_seat_occupied(seat_matrix, row, column, [0,-1], is_line_of_sight)
    return count

def apply_transform(seat_matrix, MAX_NEIGHBORS, is_line_of_sight):
    num_rows = len(seat_matrix)
    num_columns = len(seat_matrix[0])
    seat_matrix_copy = []
    for row in seat_matrix:
        seat_matrix_copy.append(row.copy())

    for i in range(0,num_rows):
        for j in range(0, num_columns):
            current_loc = seat_matrix[i][j]
            if(is_floor(current_loc)): 
                continue
            count_neighbors = num_neighbors(seat_matrix, i, j, is_line_of_sight)
            is_current_empty = is_empty_seat(current_loc)
            if(not is_current_empty and count_neighbors >= MAX_NEIGHBORS ):
                seat_matrix_copy[i][j] = 'L'
            if(is_current_empty and count_neighbors == 0 ):
                seat_matrix_copy[i][j] = '#'
    return seat_matrix_copy


def count_occupied(seat_matrix):
    count = 0
    for row in seat_matrix:
        count += row.count("#")
    return count

def find_seats_when_repeat(seat_matrix, MAX_NEIGHBORS = 4, is_line_of_sight = False, should_print = True):
    while(True):
        prev_seats = seat_matrix.copy()
        if(should_print):
            for line in seat_matrix:
                print("".join(line))

        seat_matrix = apply_transform(seat_matrix, MAX_NEIGHBORS, is_line_of_sight)
        if(seat_matrix == prev_seats):
            break
    return count_occupied(seat_matrix)

def part1():
    data = read_file('data/d11.in')
    updated = list(map(lambda x: list(x), data))
    answer = find_seats_when_repeat(updated)
    print(f"Number of seats occupied based on rules for part 1: {answer}")

def part2():
    data = read_file('data/d11.in')
    updated = list(map(lambda x: list(x), data))
    answer = find_seats_when_repeat(updated, 5, True)
    print(f"Number of seats occupied based on rules for part 2: {answer}")