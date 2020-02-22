import math

database = [
{"name": "player1", "wins": 5},
{"name": "player2", "wins": 15},
{"name": "player3", "wins": 25}
]

for l in range(20):
    w = pow(l,2)
    print("level {} needs {} wins".format(l,w))

# get wins for a user and calculate level
for player in database:
    pl = math.floor(math.sqrt(player['wins'])) #round the level down to the nearest int
    wr = pow((pl + 1),2) - player['wins']
    print("{}, you are level {} and need {} wins to get to the next level".format(player['name'], pl, wr))
