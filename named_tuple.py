players = [('konchenko', 1992, 3000),
           ('tros', 1992, 10000),
           ('savchuk', 1994, 1500)]
print(players[0][2])

from collections import namedtuple
Player = namedtuple('Player', 'name, age, rating')
players = [Player('konchenko', 1992, 3000),
           Player('tros', 1992, 10000),
           Player('savchuk', 1994, 1500)]
print(players[0])
print(players[2].name)