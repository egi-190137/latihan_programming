n, m, p = [ int(x) for x in input().split() ]

m1, m2 = [], []
for _ in range(n):
    temp = [ int(x) for x in input().split() ]
    m1.append(temp)

for _ in range(m):
    temp = [ int(x) for x in input().split() ]
    m2.append(temp)

m3 = [ [ 0 for _ in range(p) ] for _ in range(n) ]

for i in range(n):
    for j in range(p):
        for k in range(m):
            m3[i][j] += m1[i][k] * m2[k][j]

for baris in m3:
    print(" ".join(str(bil) for bil in baris))