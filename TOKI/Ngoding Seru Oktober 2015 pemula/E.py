inputan = input().split(" ")

deret = [int(inputan[i]) for i in range(3)]

for i in range(3-1):
    idx = i
    for j in range(i+1, 3):
        if inputan[3] == "1" and deret[idx] > deret[j] or inputan[3] == "0" and deret[idx] < deret[j]:
            idx = j
    deret[i], deret[idx] = deret[idx], deret[i]

print(" ".join(map(str, deret)))