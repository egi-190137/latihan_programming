inputan = input().split()

k = int(inputan[0])

for i in range(k):
    for j in range(k):
        print(inputan[2] if j==i or j == k-i-1 else inputan[1], end="")
    print("")