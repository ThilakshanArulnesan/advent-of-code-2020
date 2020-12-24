from utils.read_file import read_file_chunks

def is_same(l1,l2):
    a = l1.copy()
    a.reverse()
    return l1 == l2 or a == l2

class Tile:
    def __init__(self, name, tiles):
        self.name = name
        self.tiles = tiles
        self.options = [[],[],[],[]]
        self.is_corner = False
        self.num_neighbors = 0
    
    def print_tile(self):
        for line in self.tiles:
            print("".join(line))
    
    def get_top(self):
        return self.tiles[0]
    
    def get_bottom(self):
        return self.tiles[len(self.tiles)-1]
    
    def get_left(self):
        l = []
        for line in self.tiles:
            l.append(line[0])
        return l

    def get_right(self):
        l = []
        for line in self.tiles:
            l.append(line[len(line)-1])
        return l

    def rotate_ccw(self, n = 1):
        rotated = []
        for i in range (0, len(self.tiles)):
            rotated.append([t[len(self.tiles)-i-1] for t in self.tiles])
        self.tiles = rotated
        if(n > 1):
            self.rotate_cw(n-1)

    def rotate_cw(self, n = 1):
        rotated = []
        for i in range (0, len(self.tiles)):
            row = [t[i] for t in self.tiles]
            row.reverse()
            rotated.append(row)
        
        self.tiles = rotated
        if(n > 1):
            self.rotate_cw(n-1)

    def flip_horizontal(self):
        flipped = []
        for i in range (0, len(self.tiles)):
            row = self.tiles[i]
            row.reverse()
            flipped.append(row)
        self.tiles = flipped
    def flip_vertical(self):
        flipped = []
        for i in range (len(self.tiles)-1, -1,-1):
            flipped.append(self.tiles[i])
        self.tiles = flipped
    
    def strip_border(self):
        stripped = []
        for i in range (1, len(self.tiles)-1):
            stripped.append([])
            for j in range(1,len(self.tiles)-1):
                stripped[i-1].append(self.tiles[i][j])
        self.tiles = stripped
        # return stripped
 

    def find_num_neighbors(self, tile_list):
        neighbors = [0,0,0,0]
        for tile in tile_list:
            if(tile.name == self.name):
                continue
            if(is_same(self.get_top(), tile.get_top())):
                neighbors[0] += 1
            if(is_same(self.get_top(), tile.get_right())):
                neighbors[0] += 1
            if(is_same(self.get_top(), tile.get_left())):
                neighbors[0] += 1
            if(is_same(self.get_top(), tile.get_bottom())):
                neighbors[0] += 1

            if(is_same(self.get_right(), tile.get_top())):
                neighbors[1] += 1
            if(is_same(self.get_right(), tile.get_right())):
                neighbors[1] += 1
            if(is_same(self.get_right(), tile.get_left())):
                neighbors[1] += 1
            if(is_same(self.get_right(), tile.get_bottom())):
                neighbors[1] += 1

            if(is_same(self.get_bottom(), tile.get_top())):
                neighbors[2] += 1
            if(is_same(self.get_bottom(), tile.get_right())):
                neighbors[2] += 1
            if(is_same(self.get_bottom(), tile.get_left())):
                neighbors[2] += 1
            if(is_same(self.get_bottom(), tile.get_bottom())):
                neighbors[2] += 1

            if(is_same(self.get_left(), tile.get_top())):
                neighbors[3] += 1
            if(is_same(self.get_left(), tile.get_right())):
                neighbors[3] += 1
            if(is_same(self.get_left(), tile.get_left())):
                neighbors[3] += 1
            if(is_same(self.get_left(), tile.get_bottom())):
                neighbors[3] += 1
        s = 0
        for n in neighbors:
            s += n
        if(s == 2):
            self.is_corner = True
        self.num_neighbors = s
        return neighbors

def part1():
    data = read_file_chunks('data/d20.in')

    tile_list = []
    for chunk in data:
        tile = Tile(int(chunk[1][0:-1]), [list(a) for a in chunk[2:]])
        tile_list.append(tile)
        
    list_to_mult = []
    prod = 1
    for tile in tile_list:
        count = tile.find_num_neighbors(tile_list)
        if(count == 2):
            list_to_mult.append(tile.name)
            prod *= tile.name
    print(f"Product of count for all neighbors {prod}")

def part2():
    data = read_file_chunks('data/d20.in')
    tile_list = []
    for chunk in data:
        tile = Tile(int(chunk[1][0:-1]), [list(a) for a in chunk[2:]])
        tile_list.append(tile)
    mtx_size = int(len(data) ** 0.5)
    ordered_tiles = [[] for i in range(0, mtx_size)]
    corner_found = False

    for tile in tile_list:
        neigh = tile.find_num_neighbors(tile_list)
        # The first corner found we're going to assign to the top left.
        # This assumption is fine as we will later rotate/flip the entire map
        # so it is irrelevant which corner is where.
        if(tile.is_corner and not corner_found):
            tile.flip_horizontal()
            
            while(neigh[1] != 1 or neigh[2] != 1):
                tile.rotate_ccw()
                neigh = tile.find_num_neighbors(tile_list)
            ordered_tiles[0].append(tile)
            corner_found = True

    # Idea here: Build the entire map starting from the top-left corner (found in last step). As we move left to right
    # find a tile that matches the right boundary of the last found tile. When we move to a new row we match to the bottom
    # border of the tile on the previous row. We can optimize a bit by only consider tiles based on if they are corner, edge
    # or center pieces (based on the number of neighbors we've found they have). Also we store an `unused_tile_set` to avoid
    # reconsidering the same piece
    used_tile_set = set()
    for i in range(0,mtx_size):
        for j in range(0,mtx_size):
            expected_n = 4
            if(i == 0 or i == mtx_size-1):
                expected_n -=1
            if(j==0 or j == mtx_size-1):
                expected_n -=1

            if(i == 0 and j == 0):
                continue
            if(j == 0):
                above_tile = ordered_tiles[i-1][j]
                b = above_tile.get_bottom()
                tile_to_add = None

                for tile in tile_list:
                    if(tile.num_neighbors != expected_n):
                        continue
                    if(tile.name in used_tile_set):
                        continue
                    if(tile.get_left() == b):
                        tile.rotate_cw()
                        tile.flip_horizontal()
                        tile_to_add = tile
                        break
                    if(tile.get_top() == b):
                        tile_to_add = tile
                        break
                    if(tile.get_right() == b):
                        tile.rotate_ccw()
                        tile_to_add = tile
                        break
                    if(tile.get_bottom() == b):
                        tile.rotate_cw(2)
                        tile.flip_horizontal()
                        tile_to_add = tile
                        break

                    left_inv = tile.get_left().copy()
                    left_inv.reverse()
                    if(left_inv == b):
                        tile.rotate_cw()
                        tile_to_add = tile
                        break

                    top_inv = tile.get_top().copy()
                    top_inv.reverse()
                    if(top_inv == b):
                        tile.flip_horizontal()
                        tile_to_add = tile
                        break

                    right_inv = tile.get_right().copy()
                    right_inv.reverse()
                    if(right_inv == b):
                        tile.rotate_ccw()
                        tile.flip_horizontal()
                        tile_to_add = tile
                        break

                    bot_inv = tile.get_bottom().copy()
                    bot_inv.reverse()
                    if(bot_inv == b):
                        tile.rotate_cw(2)
                        tile_to_add = tile
                        break
                ordered_tiles[i].append(tile_to_add)
                used_tile_set.add(tile.name)
                continue
            # Find the tile that matches to the left of it
            left_tile = ordered_tiles[i][j-1]
            r = left_tile.get_right()
            
            tile_to_add = None
            # Holy this is awful
            for tile in tile_list:
                if(tile.num_neighbors != expected_n):
                    continue
                if(tile.name in used_tile_set):
                    continue
                if(tile.get_left() == r):
                    tile_to_add = tile
                    break
                if(tile.get_top() == r):
                    tile.rotate_ccw()
                    tile.flip_vertical()
                    tile_to_add = tile
                    break
                if(tile.get_right() == r):
                    tile.rotate_cw(2)
                    tile.flip_vertical()
                    tile_to_add = tile
                    break
                if(tile.get_bottom() == r):
                    tile.rotate_cw()
                    tile_to_add = tile
                    break

                left_inv = tile.get_left().copy()
                left_inv.reverse()
                if(left_inv == r):
                    tile.flip_vertical()
                    tile_to_add = tile
                    break

                top_inv = tile.get_top().copy()
                top_inv.reverse()
                if(top_inv == r):
                    tile.rotate_ccw()
                    tile_to_add = tile
                    break

                right_inv = tile.get_right().copy()
                right_inv.reverse()
                if(right_inv == r):
                    tile.rotate_cw(2)
                    tile_to_add = tile
                    break

                bot_inv = tile.get_bottom().copy()
                bot_inv.reverse()
                if(bot_inv == r):
                    tile.rotate_cw()
                    tile.flip_vertical()
                    tile_to_add = tile
                    break
            used_tile_set.add(tile.name)
            ordered_tiles[i].append(tile_to_add)
    
    for tile_list in ordered_tiles:
        for tile in tile_list:
            tile.strip_border()
            
    full_map=[]
    for i in range(0,len(ordered_tiles)):
        tile_list = ordered_tiles[i]
        for j in range (0, len(tile_list[0].tiles[0])):
            s=[]
            for k in range (0, mtx_size):
                s += tile_list[k].tiles[j]
            full_map.append(s)
            
    full_map_tile = Tile('full_map', full_map)
    sea_monster = [
     ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','#','x'],
     ['#','x','x','x','x','#','#','x','x','x','x','#','#','x','x','x','x','#','#','#'],
     ['x','#','x','x','#','x','x','#','x','x','#','x','x','#','x','x','#','x','x','x'],
    ]

    # Stores indices of '#'
    sea_monster_indices = [
        [18],
        [0, 5, 6, 11, 12, 17, 18, 19],
        [1, 4, 7, 10, 13, 16],
    ]
    num_water_per_sea_monster = len(sea_monster_indices[0]) + len(sea_monster_indices[1]) + len(sea_monster_indices[2])
    sea_monster_width  = len(sea_monster[0])

    count_monsters = 0
    counter = 0
    # Finds number of sea monsters
    while(count_monsters == 0): # Keep rotating/flipping until a sea monster is found
        full_map =  full_map_tile.tiles
        for i in range(1,len(full_map)-1):
            line = full_map[i]
            for j in range(0,len(line)-sea_monster_width):
                is_monster = True
                #check line 2 first since it has the most '#'
                for k in sea_monster_indices[1]:
                    if(line[j+k] != '#'):
                        is_monster = False
                        break
                if(not is_monster):
                    continue

                for k in sea_monster_indices[0]:
                    if(full_map[i-1][j+k] != '#'):
                        is_monster = False
                        break
                for k in sea_monster_indices[2]:
                    if(full_map[i+1][j+k] != '#'):
                        is_monster = False
                        break
                
                if(is_monster):
                    count_monsters += 1

        # Not the best way to go through all possiblities
        full_map_tile.rotate_cw()
        if(counter % 8 == 0):
            full_map_tile.flip_vertical()
        elif(counter % 4 == 0):
            full_map_tile.flip_horizontal()
        counter += 1
        
    # Assumes sea monsters can't overlap
    count_hash = 0
    for line in full_map:
        count_hash += line.count('#')
    num_not_sea_monster = count_hash-num_water_per_sea_monster*count_monsters
    print(f"The number of '#' that are not part of a sea monster are {num_not_sea_monster}")