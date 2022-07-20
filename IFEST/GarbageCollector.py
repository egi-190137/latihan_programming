[n, x, y] = list(map(int, input().split()))

garbages = []
for _ in range(n):
    garbages.append(list(map(int, input().split())))

arah = {}
for garbage in garbages:
    if garbage[0] == x:
        key = ("infinity", (garbage[1] > y))
        if key in arah.keys():
            arah[key] += garbage[2]
        else:
            arah[key] = garbage[2]
    else:
        key = ((garbage[1] - y) / (garbage[0] - x), (garbage[0] > x))
        if key in arah.keys():
            arah[key] += garbage[2]
        else:
            arah[key] = garbage[2]

terbanyak = 0
for a in arah.keys():
    if arah[a] > terbanyak:
        terbanyak = arah[a]

print(terbanyak)