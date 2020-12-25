from utils.read_file import read_file_chunks

def play_round(p1, p2):
    c1 = p1.pop()
    c2 = p2.pop()
    if(c1>c2):
        p1.insert(0,c1)
        p1.insert(0,c2)
    if(c2>c1):
        p2.insert(0,c2)
        p2.insert(0,c1)


def part1():
    data = read_file_chunks('data/d22.in')
    my_cards = list(map(lambda x: int(x), data[0][2:]))
    crab_cards = list(map(lambda x: int(x), data[1][2:]))
    my_cards.reverse()
    crab_cards.reverse()
    
    while(len(my_cards) >0 and len(crab_cards) > 0 ):
        play_round(my_cards,crab_cards)
    
    winning_cards = my_cards + crab_cards
    
    score = 0
    for i in range(0,len(winning_cards)):
        score += (i+1) * winning_cards[i]
    print(f"Score of winning player: {score}")

def play_recursive_round(p1, p2, c1, c2):
    p1_len = len(p1)
    p2_len = len(p2)

    if(p1_len >= c1 and p2_len >= c2):
        card_p1_starts = len(p1) - c1 if len(p1) - c1 > 0 else 0
        card_p2_starts = len(p2) - c2 if len(p2) - c2 > 0 else 0
        
        [winner, _] = play_game(p1[card_p1_starts:].copy(),p2[card_p2_starts:].copy())
        if(winner == "p1"):
            p1.insert(0,c1)
            p1.insert(0,c2)
        else:
            p2.insert(0,c2)
            p2.insert(0,c1)
        return
    if(c1>c2):
        p1.insert(0,c1)
        p1.insert(0,c2)
    if(c2>c1):
        p2.insert(0,c2)
        p2.insert(0,c1)

def get_string(p1,p2,c1,c2):
    return f"{p1} {p2} {c1} {c2}"

def play_game(player1, player2):
    seen_set = set()
    while(len(player1) > 0 and len(player2) > 0):
        c1 = player1.pop()
        c2 = player2.pop()
        seen_string = get_string(player1,player2,c1,c2)
        if(seen_string in seen_set):
            # player 1 wins by default
            player1.insert(0,c1)
            player1.insert(0,c2)
            winner = "p1"
            return [winner, player1 + player2]
        seen_set.add(seen_string)
        play_recursive_round(player1,player2,c1,c2)
    if(len(player1) == 0):
        winner = "p2"
    else:
        winner = "p1"
    return [winner, player1 + player2]

def part2():
    data = read_file_chunks('data/d22.in')
    my_cards = list(map(lambda x: int(x), data[0][2:]))
    crab_cards = list(map(lambda x: int(x), data[1][2:]))
    my_cards.reverse()
    crab_cards.reverse()

    [winner, winning_cards] =  play_game(my_cards, crab_cards)
    
    score = 0
    for i in range(0,len(winning_cards)):
        score += (i+1) * winning_cards[i]
    print(f"Winner is {winner} with a score of winning player: {score}")