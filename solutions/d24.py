from utils.read_file import read_file
import math

PI = math.pi

class Hexagon:
    def __init__(self, x, y, is_black = False):
        self.is_black = is_black
        self.x = x
        self.y = y
        self.num_neighbors = 0
    
    def add_neighbor(self):
        self.num_neighbors += 1

    def reset_neighor(self):
        self.num_neighbors = 0

    def get_neighbor_coords(self):
        neighbors = []
        neighbors.append([self.x-1, self.y])
        neighbors.append([self.x+1, self.y])
        neighbors.append([ round(self.x + math.cos(PI/3), 4),round( self.y + math.sin(PI/3), 4)])
        neighbors.append([round(self.x + math.cos(PI/3), 4),  round(self.y - math.sin(PI/3), 4)])
        neighbors.append([ round(self.x - math.cos(PI/3), 4),  round(self.y + math.sin(PI/3), 4)])
        neighbors.append([round(self.x - math.cos(PI/3), 4),  round(self.y - math.sin(PI/3), 4)])
        return neighbors

def parse_string(instructions):
    i = 0
    instr_list = []
    while(i<len(instructions)):
        char = instructions[i]
        if(char == "n" or char == "s"):
            instr_list.append(char + instructions[i+1])
            i+=2
        else:
            instr_list.append(char)
            i+=1
    return instr_list


def get_coords(c):
    # Handle -0 = 0 case
    n1 = round(c[0],3) if round(c[0],3) != 0 else 0
    n2 = round(c[1],3) if round(c[1],3) != 0 else 0
    return f"{n1},{n2}"

def part1():
    data = read_file('data/d24.in')
    tile_dict = {}
    for line in data:
        st = parse_string(line)
        coords = [0,0]
        for instr in st:
            if(instr == "w"):
                coords[0] -= 1
            if(instr == "e"):
                coords[0] += 1
            if(instr == "ne"):
                coords[0] += round(math.cos(PI/3),3)
                coords[1] += round(math.sin(PI/3),3)
            if(instr == "se"):
                coords[0] += round(math.cos(PI/3),3)
                coords[1] -= round(math.sin(PI/3),3)
            if(instr == "nw"):
                coords[0] -= round(math.cos(PI/3),3)
                coords[1] += round(math.sin(PI/3),3)
            if(instr == "sw"):
                coords[0] -= round(math.cos(PI/3),3)
                coords[1] -= round(math.sin(PI/3),3)
        str_coords = get_coords(coords)
        if(str_coords in tile_dict):
            tile_dict[str_coords].is_black = not tile_dict[str_coords].is_black
        else:
            new_tile = Hexagon(coords[0],coords[1], True)
            tile_dict.update({str_coords: new_tile})
        count = 0
    for tile_str in tile_dict:
        tile = tile_dict[tile_str]
        if(tile.is_black):
            count += 1

    print(f"Number of tiles flipped to black {count}")


def part2():
    data = read_file('data/d24.in')
    tile_dict = {}
    NUM_DAYS = 100

    for line in data:
        st = parse_string(line)
        coords = [0,0]
        for instr in st:
            if(instr == "w"):
                coords[0] -= 1
            if(instr == "e"):
                coords[0] += 1
            if(instr == "ne"):
                coords[0] = round(coords[0] + math.cos(PI/3), 4)
                coords[1] = round(coords[1] + math.sin(PI/3), 4)
            if(instr == "se"):
                coords[0] = round(coords[0] + math.cos(PI/3), 4)
                coords[1] = round(coords[1] - math.sin(PI/3), 4)
            if(instr == "nw"):
                coords[0] = round(coords[0] - math.cos(PI/3), 4)
                coords[1] = round(coords[1] + math.sin(PI/3), 4)
            if(instr == "sw"):
                coords[0] = round(coords[0] - math.cos(PI/3), 4)
                coords[1] = round(coords[1] - math.sin(PI/3), 4)
            s_coords = get_coords(coords)
            if(s_coords not in tile_dict):
                new_tile = Hexagon(coords[0],coords[1])
                tile_dict.update({s_coords: new_tile})
                
        str_coords = get_coords(coords)
        if(str_coords in tile_dict):
            tile_dict[str_coords].is_black = not tile_dict[str_coords].is_black
        else:
            new_tile = Hexagon(coords[0],coords[1], True)
            tile_dict.update({str_coords: new_tile})
    for day in range(1,NUM_DAYS+1): 
        neighbors_to_add = []
        for tile_str in tile_dict:
            tile = tile_dict[tile_str]
            if(tile.is_black):
                neighbors_to_add += tile.get_neighbor_coords()

        for neighbor in neighbors_to_add:
            str_coords = get_coords(neighbor)
            if(str_coords in tile_dict):
                tile = tile_dict[str_coords]
                tile.add_neighbor()
            else:
                tile = Hexagon(neighbor[0],neighbor[1])
                tile.add_neighbor()
                tile_dict.update({str_coords: tile})

        count = 0
        for str_coords in tile_dict:
            tile = tile_dict[str_coords]
            if(tile.is_black):
                if(tile.num_neighbors == 0 or tile.num_neighbors > 2):
                    tile.is_black = False
            else:
                if(tile.num_neighbors == 2):
                    tile.is_black = True
            tile.reset_neighor()

            if(tile.is_black):
                count += 1

    print(f"After day {NUM_DAYS} the of tiles flipped to black {count}")
