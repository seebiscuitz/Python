import math
import player
import gameinfo
import trueskill
import numpy as np

player_num = 5
players=[]
players_hist = player_num * []

# creates game
ngame=gameinfo.game(25)

# creates players
for i in range(player_num):
    players.append(player.player(i))
#

# test game
# win = 1, draw = 0, loss = -1
# assume p1 wins and p2 losses
p1_res = trueskill.trueskillcalc(ngame, players[0], players[1], 1)
p2_res = trueskill.trueskillcalc(ngame, players[0], players[1], -1)
players[0].update(1,p1_res[0],p1_res[1])
players[1].update(1,p2_res[0],p2_res[1])

print(players[0].meanhist)
print(players[1].meanhist)