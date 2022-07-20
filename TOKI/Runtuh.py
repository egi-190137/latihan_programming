baris, kolom = [ int(x) for x in input().split() ]

papan = []
for _ in range(baris):
    papan.append([ x for x in input() ])

isRuntuh = False
while not isRuntuh:
    first = True
    for i in range(len(papan) - 1, -1, -1):
        if papan[i] == ["1" for i in range(kolom)]:
            papan[i] = ["0" for i in range(kolom)]
            if first:
                idx = i
            first = False
