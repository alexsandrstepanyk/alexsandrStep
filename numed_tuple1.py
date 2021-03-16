gamers = [('victorovich', 1970, 2000),
          ('konchenko', 1991, 2001),
          ('petruk', 1994, 2002)]
print(gamers[1][1])
from  collections import namedtuple
gamer = namedtuple('gamer', 'name, age, rating')
gamers = [gamer('sachuk', 1994, 1994),
          gamer('victorovich', 1970, 2000),
          gamer('konchenko', 1991, 2001),
          gamer('petruk', 1994, 2002)]
print(gamers[0].age )
print(gamers[2].name)
#gamers.append('gorbaruk', 1994, 2001)
print(gamers)