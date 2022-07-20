from math import sqrt, pow

points = []
for i in range(3):
    coordinate = tuple( int(x) for x in input().split() )
    points.append(coordinate)

lengths = []
for i in range(3):
    for j in range(i+1, 3):
        length = sqrt(pow(points[j][0] - points[i][0], 2) + pow(points[j][1] - points[i][1], 2))
        lengths.append(length)
    
lengthTotal = sum(lengths)
isTriangle = True
for i in range(len(lengths)):
    if lengthTotal - lengths[i] <= lengths[i]:
        isTriangle = False
        break

if not isTriangle:
    print("-1")
else:
    tegak = False
    for i in range(3):
        for j in range(i+1, 3):
            if points[i][0] == points[j][0]:
                tegak = True
                break
    
    if tegak:
        print("1")
    else:
        print("0")
