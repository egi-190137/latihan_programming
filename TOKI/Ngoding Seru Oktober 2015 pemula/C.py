n = int(input())
nomor = input().split(" ")

for i in range(n-1, -1, -1):
    print(nomor[i], end=("," if i > 0 else "\n"))