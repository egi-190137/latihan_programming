n = int(input())

arr = []
for _ in range(n):
    temp = input().split()
    arr.append([temp[0][1:], int(temp[1])])
# print(arr)

panjang = len(arr[0][0])
terbesar = 0
namaTerbesar = ''
idx = 0
while panjang > 1 and idx < len(arr) - 1:
    # ketemu = False
    
    for i in range(len(arr[idx][0]) - panjang + 1):
        temp = 0
        for item in arr:
            if arr[idx][0][i:panjang+i] in item[0]:
                temp += item[1]

        if temp > terbesar:
            terbesar = temp
            namaTerbesar = arr[idx][0][i:panjang+i]

    panjang -= 1
    if panjang == 1:
        idx += 1
        panjang = len(arr[idx][0])

# itemTerbesar = 0
# for i in range(1, len(arr)):
#     if arr[itemTerbesar][1] < arr[i][1]:
#         itemTerbesar = i

# if arr[itemTerbesar][1] > terbesar:
#     print(f'V{arr[itemTerbesar][0]}')
# else:
print(f'V{namaTerbesar}')