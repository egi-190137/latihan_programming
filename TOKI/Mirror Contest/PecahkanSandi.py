n, m = [ int(x) for x in input().split() ]

a = [ int(x) for x in input().split() ]
b = [ int(x) for x in input().split() ]

fkTerbesar = 0
for k in range(m):
    fk = 0
    for i in range(n):
        fk += ( (a[i] + k) % m ) * b[i]
    
    if fk > fkTerbesar:
        fkTerbesar = fk

print(fkTerbesar)