n, d = [ int(x) for x in input().split() ]

t = []
jarak = []
for _ in range(n):
    t.append( [ int(x) for x in input().split() ] )

for i in range(len(t) - 1):
    for j in range(i+1, len(t)):
        temp = abs( t[i][0] - t[j][0] ) ** d + abs( t[i][1] - t[j][1] ) ** d
        jarak.append(temp)

terbesar = jarak[0]
terkecil = jarak[0]
for i in range(1, len(jarak)):
    if jarak[i] > terbesar:
        terbesar = jarak[i]
    elif jarak[i] < terkecil:
        terkecil = jarak[i]

print(f"{terkecil} {terbesar}")