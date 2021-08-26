stringAngka = input().split(" ")

n, d = int(stringAngka[0]), int(stringAngka[1])

listDna = []
for i in range(n):
    listDna.append(int(input()))

sorted(listDna)
jumlahKel = 1
for i in range(len(listDna) - 1):
    if abs(listDna[i] - listDna[i+1]) >= d:
        jumlahKel += 1

print(jumlahKel)
