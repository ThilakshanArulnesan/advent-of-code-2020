def part1():
    # ints = [3,8,9,1,2,5,4,6,7]
    ints = [1,5,7,6,2,3,9,8,4]
    cur = 0
    move = 1
    while(move<=100):
        to_move = []
        to_move.append(ints[(cur+1) % 9])
        to_move.append(ints[(cur+2) % 9])
        to_move.append(ints[(cur+3) % 9])
        
        pos_to_move_to = ints[cur]-1 if ints[cur]-1 != 0 else 9
        while(pos_to_move_to in to_move):
            pos_to_move_to -= 1
            if(pos_to_move_to == 0):
                pos_to_move_to = 9

        new_ints = []
        for i in range(0, len(ints)):
            num = ints[i]
            if(num in to_move):
                continue
            new_ints.append(num)
            if(num == pos_to_move_to):
                new_ints += to_move
        cur = new_ints.index(ints[cur])
        ints = new_ints
        move += 1
        cur = (cur + 1) % 9
    s = "".join([f"{i}" for i in ints])
    pos_of_1 = s.find("1")
    print(f"Final position after 100 moves: {s[pos_of_1+1:]}{s[0:pos_of_1]}")

# Singly linked-list
class Node:
    def __init__(self,value, right=None):
        self.right = right
        self.value = value

def part2():
    ints = [1,5,7,6,2,3,9,8,4]
    for i in range(10,1000001):
        ints.append(i)
    # Build list
    cur = Node(ints[0])
    nodes = [cur]
    SIZE = len(ints)
    for i in range(1,len(ints)):
        next = Node(ints[i])
        nodes[i-1].right = next
        nodes.append(next)

    node_dict = {}

    for node in nodes:
        node_dict.update({node.value: node})
    print("Dictionary has been built")
    nodes[len(nodes)-1].right  = nodes[0]

    # Perform steps
    count = 1
    while(count <= 10000000):
        # Remove next three
        values_removed = [
            cur.right.value,
            cur.right.right.value,
            cur.right.right.right.value,
        ]

        # Find to place the removed nodes:
        num_to_find = cur.value-1 if cur.value-1 != 0 else SIZE 
        while(num_to_find in values_removed):
            num_to_find -= 1
            if(num_to_find == 0):
                num_to_find = SIZE
        
        picked_up = cur.right # Left most node of the three removed nodes
        cur.right = cur.right.right.right.right # Link the current node to the next node that hasn't been removed
        dest = node_dict[num_to_find] # Get the node where we need to insert, use a dictionary to save time (O(n) lookup for each iteration otherwise, where n is the size of the linked list)

        # Perform the insertion
        temp = dest.right
        dest.right = picked_up
        picked_up.right.right.right = temp

        # Move to the next node and repeat
        count += 1
        cur = cur.right

    loc_of_1 = cur
    # Iterate through the linked list until we find position 1
    while(True):
        if(loc_of_1.value == 1):
            break
        else:
            loc_of_1 = loc_of_1.right
        
    print(f"After 10,000,000 operations, the product of the two numbers after 1 is {loc_of_1.right.value * loc_of_1.right.right.value}")