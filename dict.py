players = {
    'zett' : 1994,
    'bober' : 1990,
    'vaschuk' : 2000,
    'petruk' : 1972
}
players = dict(zett=1994, bober=1990, vaschuk=2000, petruk=1972)
print(players)

pip = players['zett']
print(f"happy birthday zett is  {pip}")

players.get('petruk')
print(players.get('petruk'))
players ['sirko'] = 2001
print(players)
del players['sirko']
print(players)
keys = players.keys()
print(type(keys))
print(keys)
l = list(players.keys())
print(type(l))
print(l)
sorted(players.keys())
print('zett' in players)
print('petruk'  not in  players)
vals = players.values()
print(type(vals))
print(vals)
vals = list(players.values())
print(type(vals))
print(vals)
sorted(players.values())
print(sorted(players.values()))
players_copy = players.copy()
print(players_copy)
players_copy ['ivan'] = 1991
print(players_copy)
print(players)

for k, v in players_copy.items():
    print(k, v)
items = players.items()
print(type(players.items()))
players_copy.pop('ivan')
print(players_copy)
players_copy ['koncheniy'] = 1972
print(players_copy)