import math
import player
import gameinfo
import trueskill
import margin
import gaussdist
from numpy import random


# define a game
def _game_(p1, p2):
    # Normal difference distribution to give performance difference distribution 
    # sigma and mean from https://mathworld.wolfram.com/NormalDifferenceDistribution.html
    if p1.mean > p2.mean:
        ngame_mean = p1.mean - p2.mean
        ngame_stdv = math.sqrt(math.pow(p1.stdv,2) + math.pow(p2.stdv,2))
        p1_loss = gaussdist.at(0, ngame_mean, ngame_stdv)
    else:
        ngame_mean = p2.mean - p1.mean
        ngame_stdv = math.sqrt(math.pow(p2.stdv,2) + math.pow(p1.stdv,2))
        p1_loss = 1 - gaussdist.at(0, ngame_mean, ngame_stdv)
    
    # P1 rolls a random number
    p1_rand = random.rand()
    if p1_rand == p1_loss:
        # draw
        result = 0
    elif p1_rand >= p1_loss:
        # p1 win
        result = 1
    else:
        # p1 loss
        result = -1
    
    # Update results
    p1_res = trueskill.trueskillcalc(ngame, p1, p2, result)
    p2_res = trueskill.trueskillcalc(ngame, p1, p2, -result)
    p1.update(result,p1_res[0],p1_res[1])
    p2.update(result,p2_res[0],p2_res[1])

    return 

round_counter = 0
max_wins_tmp = 0
max_win_id = 0
player_num = 32
max_wins = 100
max_wins_ach = False
players=[]
players_hist = player_num * []
player_pairs = [[[],[]] for i in range(int(player_num / 2))]
#id_arr = list(range(player_num))

# creates game
ngame=gameinfo.game(25)

# creates players
for i in range(player_num):
    players.append(player.player(i))
#

while not max_wins_ach:
    # create a copy of the players array
    nums = list(range(player_num)).copy()
    # pair off players
    for i in range(len(player_pairs)):
        # pick first player
        p1 = random.choice(nums)
        nums.remove(p1)
        # pick second player
        p2 = random.choice(nums)
        nums.remove(p2)
        # add to pairs list
        player_pairs[i][0] = p1
        player_pairs[i][1] = p2
    # play all of the games in the round
    for i in range(len(player_pairs)):
        _game_(players[player_pairs[i][0]],players[player_pairs[i][1]])
    # check for winner
    round_counter += 1
    for i in range(len(players)):
        if players[i].win > max_wins_tmp:
            max_wins_tmp = players[i].win
            max_win_id = i
        if players[i].win == max_wins:
            max_wins_ach = True
            winner = players[i]  
    #print(players[max_win_id].id,' is leading with ',players[max_win_id].win,' wins.')
            
print('Stats Table: ')
print('Player ID    |   Wins    |   Losses  |   End Mean    |   End Stdv    |')
for i in range(len(players)):
    print(players[i].id,'   ',players[i].win,'   ',players[i].loss,'   ',players[i].mean,'   ',players[i].stdv)
print(' ')
print('Summary: ')
print(player_num,' players played ', round_counter,' rounds until one had ', max_wins, ' wins.')
print(winner.id,' won with achieving a max skill of', max(winner.meanhist))
best_wlr = 0
best_wlr_id = 0
for i in range(len(players)):
    if players[i].wlr > best_wlr:
        best_wlr = players[i].wlr
        best_wlr_id = i
print(players[best_wlr_id].id,' acheived best win/loss ratio of ', players[best_wlr_id].wlr)

