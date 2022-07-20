arr = list(map(int, input().split()))

# Mengurutkan list
for i in range(len(arr)):
    terkecil = i
    for j in range(i+1, len(arr)):
        if arr[terkecil] > arr[j]:
            terkecil = j
    [arr[i], arr[terkecil]] = [arr[terkecil], arr[i]]

# Mencari bilangan yang memiliki selisih 1
for i in range(len(arr) - 1):
    if arr[i+1] - arr[i] == 1:
        print(arr[i], arr[i+1]) 