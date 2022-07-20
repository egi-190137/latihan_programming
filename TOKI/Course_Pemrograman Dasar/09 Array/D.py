m, n = [ int(x) for x in input().split() ]

matriks = []
for _ in range(m):
    temp = [ int(x) for x in input().split() ]
    matriks.append(temp)

for i in range(n):
    for j in range(m-1, -1, -1):
        print(matriks[j][i], end=" ")
    print("")