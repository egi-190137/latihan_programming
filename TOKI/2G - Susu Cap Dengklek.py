mDanN = input().split(" ")
m, n = int(mDanN[0]), int(mDanN[1])

bDanK = input().split(" ")
b, k = int(bDanK[0]), int(bDanK[1])

for i in range(m):
    input()

hasil = 0
for i in range(b, m + 1):
    for j in range(k, n + 1):
        hasil += (m - b + 1) * (n - k + 1)

print(hasil)
