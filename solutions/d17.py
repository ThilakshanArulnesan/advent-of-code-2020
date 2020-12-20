from utils.read_file import read_file


# ..##.#.#
# .#####..
# #.....##
# ##.##.#.
# ..#...#.
# .#..##..
# .#...#.#
# #..##.##

def check():
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            for k in range(-1,2,1):
                print(i,j,k)

def has_active_cube(layer):
    for row in layer:
        for element in row:
            if(element == '#'):
                return True
    return False

def get_string_from_coords(x,y,z,w=None):
    if(w == None):
        return f"{x},{y},{z}"
    else:
        return f"{x},{y},{z},{w}"


class Cube:
    def __init__(self, is_active, x, y, z, w = None):
        self.is_active = is_active
        self.x = x
        self.y = y
        self.z = z
        if(w != None):
            self.w = w
        self.num_active_neighbors = 0

        neighbor_list = []
        if(w == None):
            for i in range(-1,2,1):
                for j in range(-1,2,1):
                    for k in range(-1,2,1):
                        if(i== 0 and j == 0 and k == 0):
                            continue
                        neighbor_list.append(get_string_from_coords(x+i,y+j,z+k))
        else:
            for i in range(-1,2,1):
                for j in range(-1,2,1):
                    for k in range(-1,2,1):
                        for l in range(-1,2,1):
                            if(i== 0 and j == 0 and k == 0 and l == 0):
                                continue
                            neighbor_list.append(get_string_from_coords(x+i,y+j,z+k, w + l))
        self.neighbor_list = neighbor_list

    def add_neighbor(self):
        self.num_active_neighbors += 1

    def reset_neighbor_count(self):
        self.num_active_neighbors = 0

    def set_active(self):
        if(self.is_active):
            self.is_active = True if (self.num_active_neighbors == 2 or self.num_active_neighbors == 3) else False
        else:
            self.is_active = True if self.num_active_neighbors == 3 else False


def part1():
    data = [list(l) for l in read_file('data/d17.in')]
    cube_dict = {}

    for i in range (0, len(data)):
        for j in range (0,len(data[0])):
            cube = Cube(data[i][j] == "#", i,j,0)
            cube_dict.update({f'{i},{j},{0}' : cube})

    count_active = 0
    for z in range(0,6):
        dict_copy = cube_dict.copy()

        for cube in dict_copy.values():
            if not cube.is_active:
                continue
            for neighbor in cube.neighbor_list:
                if(neighbor in cube_dict):
                    cube_dict[neighbor].add_neighbor()
                else:
                    x,y,z = map(lambda x: int(x),neighbor.split(","))
                    new_cube = Cube(False,x,y,z)
                    new_cube.add_neighbor()
                    cube_dict.update({f'{x},{y},{z}': new_cube})

        count_active = 0
        count_inactive = 0
        for cube in cube_dict.values():
            cube.set_active()
            if cube.is_active:
                count_active += 1
            else:
                count_inactive += 1
            cube.reset_neighbor_count()
    print(f"After 6 cycles there are {count_active} active cubes")




def part2():
    data = [list(l) for l in read_file('data/d17.in')]
    cube_dict = {}

    for i in range (0, len(data)):
        for j in range (0,len(data[0])):
            cube = Cube(data[i][j] == "#", i,j,0,0)
            cube_dict.update({f'{i},{j},{0},{0}' : cube})

    count_active = 0
    for z in range(0,6):
        dict_copy = cube_dict.copy()

        for cube in dict_copy.values():
            if not cube.is_active:
                continue
            for neighbor in cube.neighbor_list:
                if(neighbor in cube_dict):
                    cube_dict[neighbor].add_neighbor()
                else:
                    x,y,z,w = map(lambda x: int(x),neighbor.split(","))
                    new_cube = Cube(False,x,y,z,w)
                    new_cube.add_neighbor()
                    cube_dict.update({f'{x},{y},{z},{w}': new_cube})

        count_active = 0
        count_inactive = 0
        for cube in cube_dict.values():
            cube.set_active()
            if cube.is_active:
                count_active += 1
            else:
                count_inactive += 1
            cube.reset_neighbor_count()
    print(f"After 6 cycles there are {count_active} active cubes")