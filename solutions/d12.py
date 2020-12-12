
from utils.read_file import read_file

def get_vector(dir, num):
    if(dir == "N"):
        return [num * i for i in [0,1]]
    if(dir == "E"):
        return [num * i for i in [1,0]]
    if(dir == "S"):
        return [num * i for i in [0,-1]]
    if(dir == "W"):
        return [num * i for i in [-1,0]]

def parse_instr(instr):
    return instr[0], int(instr[1:])

def get_pos(instructions):
    pos = [0,0]
    dirList = ["N", "E", "S", "W"]
    curDir = 1 #Ship starts pointing E
    for instruction in instructions:
        command, num = parse_instr(instruction)
        if(command == "F"):
            incr = get_vector(dirList[curDir], num)
            pos[0] += incr[0]
            pos[1] += incr[1]
        if(command in dirList):
            incr = get_vector(command, num)
            pos[0] += incr[0]
            pos[1] += incr[1]
        if(command == "L"):
            curDir = (curDir - num // 90) % 4 # assumption 90 degree angles
        if(command == "R"):
            curDir = (curDir + num // 90) % 4 # assumption 90 degree angles

    return pos

def rotate(waypoint,angle):
    if(angle == 0):
        return waypoint
    if(angle == 90):
        #ex [3,1] -> [1, -3]
        return [waypoint[1], -waypoint[0]]
    if(angle == 180):
        #ex [3,1] -> [-3, -1]
        return [-waypoint[0], -waypoint[1]]
    if(angle == 270):
        #ex [3,1] -> [-1, 3]
        return [-waypoint[1], waypoint[0]]

def get_pos_with_waypoint(instructions):
    waypoint = [10, 1]
    pos = [0,0]
    dirList = ["N", "E", "S", "W"]

    for instruction in instructions:
            command, num = parse_instr(instruction)
            if(command == "F"):
                pos[0] += num * waypoint[0]
                pos[1] += num * waypoint[1]
            if(command in dirList):
                incr = get_vector(command, num)
                waypoint[0] += incr[0]
                waypoint[1] += incr[1]
            if(command == "L"):
                angle = -num % 360
                waypoint = rotate(waypoint, angle)
            if(command == "R"):
                angle = num % 360
                waypoint = rotate(waypoint, angle)

    return pos

def part1():
    data = read_file('data/d12.in')
    final_pos = get_pos(data)
    print(f"Manhattan distance: {abs(final_pos[0])+ abs(final_pos[1])}")
    

def part2():
    data = read_file('data/d12.in')
    final_pos = get_pos_with_waypoint(data)
    print(f"Manhattan distance: {abs(final_pos[0])+ abs(final_pos[1])}")