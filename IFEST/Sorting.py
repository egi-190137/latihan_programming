n = int(input())

angka = set(map(int, input().split()))

ganjil = []
genap = []

for a in angka:
    if a%2 == 1:
        ganjil.append(a)
    else:
        genap.append(a)

for i in range(len(ganjil) - 1):
    terkecil = i
    for j in range(i+1, len(ganjil)):
        if ganjil[terkecil] > ganjil[j]:
            terkecil = j
    [ ganjil[i], ganjil[terkecil] ] = [ ganjil[terkecil], ganjil[i] ]

for i in range(len(genap) - 1):
    terkecil = i
    for j in range(i+1, len(genap)):
        if genap[terkecil] > genap[j]:
            terkecil = j
    [ genap[i], genap[terkecil] ] = [ genap[terkecil], genap[i] ]

if len(ganjil) == len(genap):
    for i in range(len(ganjil)):
        print(genap[i], ganjil[i], end=" ")
    print("")   
elif len(ganjil) > len(genap):
    for i in range(len(genap)):
        print(ganjil[i], genap[i], end=" ")
        if i == len(genap)-1:
            print(ganjil[i+1])
else:
    for i in range(len(ganjil)):
        print(genap[i], ganjil[i], end=" ")
        if i == len(ganjil)-1:
            print(genap[i+1])