import math

database = [
{"name": "player1", "wins": 5},
{"name": "player2", "wins": 15},
{"name": "player3", "wins": 25}
]

for l in range(20):
    if l ==1:
        continue
    w = (l * (l + 1)) -2
    print("level {} needs {} wins".format(l,w))

# get wins for a user and calculate level
for player in database:
    pl = math.floor((math.sqrt(1 + (4 * (player['wins'] + 2))-1)/2)) #round the level down to the nearest int
    wr = (pl + 2)*(pl + 1) - 2 - player['wins']
    print("{}, you are level {} and need {} wins to get to the next level".format(player['name'], pl, wr))
