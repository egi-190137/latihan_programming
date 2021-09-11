n, k, c, p = [ int(x) for x in input().split() ]

a = [ int(x) for x in input().split() ]
b = [ int(x) for x in input().split() ]

for x in range(n):
    terjauh = 0
    biayaTerjauh = 0
    for y in range(n):
        jarak = abs(x-y) + 1
        if x == y:
            biaya = a[x] + b[y]
        else:
            biaya = a[x] + b[y] + c * (abs(x-y) ** p)
        
        if k >= biaya:
            if terjauh == 0 or terjauh < jarak:
                terjauh = jarak
                biayaTerjauh = biaya
            elif terjauh == jarak and biayaTerjauh > biaya:
                biayaTerjauh = biaya
    print(f'{terjauh} {k- biayaTerjauh}')