n = int(input())

arr = [[], [], []]
for i in range(n):
    temp = int(input())
    if temp < 0:
        arr[0].append(temp)
    elif temp == 0:
        arr[1].append(temp)
    else:
        arr[2].append(temp)
 
for innerList in arr:
    for num in innerList:
        print(num)