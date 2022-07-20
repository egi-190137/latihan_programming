n = int(input())

jumlah = []
for _ in range(n):
    int(input())
    temp = input().split()
    hitung = 0
    for i in range(1, len(temp)):
        if temp[i] != temp[i-1]:
            hitung+=1
    jumlah.append(hitung)

for j in jumlah:
    print(j)
