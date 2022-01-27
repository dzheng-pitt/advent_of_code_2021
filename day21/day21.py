import numpy as np

def roll_dice(dice):
    moves = 0
    for i in range(3):
        if dice == 101:
            dice = 1
        moves += dice
        dice += 1
        
    return moves, dice

def move_player(player, dice):
    moves, dice = roll_dice(dice)
    player['pos'] = (player['pos'] + moves) % 10
    player['score'] += player['pos'] + 1
    
    return dice


if __name__ == '__main__':

    # part 1
    
    # {board position, points}
    # use 0 indexing for board position for convenience with mod
    # 0 -> 1
    # 1 -> 2
    # ...
    # 9 -> 10
    
    players = [{'pos':0,'score':0},{'pos':5,'score':0}]
    
    dice = 1
    dice_rolls = 0
    
    i = 0
    while players[0]['score'] < 1000 and players[1]['score'] < 1000:
        
        player = players[i]
        dice = move_player(player, dice)
        dice_rolls += 3
        i = (i + 1) % 2
    
    print(dice_rolls*min(players[0]['score'],players[1]['score']))
    


    # part 2
    
    # consider all possible rolls from one turn of the game
    universe_rolls = []
    
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                universe_rolls.append(i+j+k)
    
    moves, counts = np.unique(universe_rolls, return_counts=True)
    
    # given a player's position and the roll of die from the universe,
    # this is the resulting score
    scores = {}
    for i in range(0,10):
        for j in universe_rolls:
            scores[(i,j)] = ((i + j) % 10) + 1
    
    # init the game
    # queue is {((player1 pos, player1 score),(player2 pos, player2 score)):count of universes}
    player1_queue = {((0,0),(5,0)):1} 
    player2_queue = {}
    player1_scores = 0
    player2_scores = 0
    while True:
        
        # for each unresolved scenario in player1's universe queue, play
        # a turn and queue up the resulting scenarios for player 2. Resolve
        # wins
        while len(player1_queue) > 0:
            scenario = list(player1_queue.keys())[0]
            universes = player1_queue.pop(scenario)
            
            p1_info = scenario[0]
            p2_info = scenario[1]
            
            for i in range(len(moves)):
                new_p1_score = scores[(p1_info[0],moves[i])] + p1_info[1]
                new_p1_pos = (p1_info[0]+moves[i]) % 10
                new_tuple = ((new_p1_pos,new_p1_score),(p2_info[0],p2_info[1]))
                if new_p1_score >= 21:
                    player1_scores += universes*counts[i]
                elif new_tuple in player2_queue:
                    player2_queue[new_tuple] += universes*counts[i]
                else:
                    player2_queue[new_tuple] = universes*counts[i]
         
        # do similarly for player two
        while len(player2_queue) > 0:
            
            scenario = list(player2_queue.keys())[0]
            universes = player2_queue.pop(scenario)
            
            p1_info = scenario[0]
            p2_info = scenario[1]
            
            for i in range(len(moves)):
                new_p2_score = scores[(p2_info[0],moves[i])] + p2_info[1]
                new_p2_pos = (p2_info[0]+moves[i]) % 10
                new_tuple = ((p1_info[0],p1_info[1]),(new_p2_pos,new_p2_score))
                if new_p2_score >= 21:
                    player2_scores += universes*counts[i]
                elif new_tuple in player1_queue:
                    player1_queue[new_tuple] += universes*counts[i]
                else:
                    player1_queue[new_tuple] = universes*counts[i]
        
        # quit if no more universes to resolve
        if len(player1_queue) == 0:
            break
    
        
    print(player1_scores, player2_scores)
