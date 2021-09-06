n = int(input())

arr = []
for i in range(n):
    arr.append(int(input("? " + str(i+1) + " ")))

x = 1
for i in range(1, n-1):
    if arr[i-1] == arr[i]:
        x += 1
    else:
        x = 1

a = 0
if arr[0] == 1:
    while arr[:x] != [1 for i in range(x)]:
        arr.insert(0, 1)
        a+=1

while arr[:x] != [0 for i in range(x)]:
    arr.insert(0, 0)
    a += 1

b = 0
if arr[len(arr) - 1] == 0:
    while arr[-x:] != [0 for i in range(x)]:
        arr.append(0)
        b += 1

while arr[-x:] != [1 for i in range(x)]:
    arr.append(1)
    b += 1

y = len(arr) // (x * 2)
print("!", x, y, a, b)