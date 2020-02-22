import math

database = [
{"name": "player1", "wins": 5},
{"name": "player2", "wins": 15},
{"name": "player3", "wins": 25}
]

levels = [ 0, 3, 6, 9, 12, 17, 23, 28, 32, 40, 48]

for l,w in enumerate(levels):
    print("level {} needs {} wins".format((l+1),w))

# get wins for a user and calculate level
#because our array starts from 0, pl is actually the index of the nth +1 element
for player in database:
    pl = levels.index(min(i for i in levels if i > player['wins']))
    wr = levels[pl] - player['wins']
    print("{}, you are level {} and need {} wins to get to the next level".format(player['name'], pl, wr))
