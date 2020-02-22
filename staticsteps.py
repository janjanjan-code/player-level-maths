import math

database = [
{"name": "player1", "wins": 5},
{"name": "player2", "wins": 15},
{"name": "player3", "wins": 25}
]

c = 10
for l in range(20):
    w = l * c
    print("level {} needs {} wins".format(l,w))

# get wins for a user and calculate level
for player in database:
    pl = math.floor(player['wins'] / c) #round the level down to the nearest int
    wr = ((pl + 1) * c) - player['wins']
    print("{}, you are level {} and need {} wins to get to the next level".format(player['name'], pl, wr))
