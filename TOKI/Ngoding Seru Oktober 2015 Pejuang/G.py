n = int(input())
arr = [int(x) for x in input().split()]

plus = 0
minus = 0
nol = 0
for x in arr:
    if x == 0:
        nol += 1
    elif x > 0:
        plus += 1
    else:
        minus += 1

if nol >= len(arr)//2:
    for i in range(len(arr) - 1):
        if i%2 == 0 and arr[i] == 0:
            for j in range(i+1, len(arr)):
                if arr[j] != 0:
                    [arr[i], arr[j]] = [arr[j], arr[i]]
                    break
        elif i%2 == 1 and arr[i] != 0:
            for j in range(i+1, len(arr)):
                if arr[j] == 0:
                    [arr[i], arr[j]] = [arr[j], arr[i]]
                    break
    for i in range(len(arr)):
        if i < len(arr)-1:
            print(arr[i], end=" ")
        else:
            print(arr[i])

elif minus >= len(arr)//2:
    for i in range(len(arr) - 1):
        if i%2 == 0 and arr[i] < 0:
            for j in range(i+1, len(arr)):
                if arr[j] >= 0:
                    [arr[i], arr[j]] = [arr[j], arr[i]]
                    break
        elif i%2 == 1 and arr[i] >= 0:
            for j in range(i+1, len(arr)):
                if arr[j] < 0:
                    [arr[i], arr[j]] = [arr[j], arr[i]]
                    break
    for i in range(len(arr)):
        if i < len(arr)-1:
            print(arr[i], end=" ")
        else:
            print(arr[i])

elif minus == len(arr) or plus == len(arr) or nol == len(arr): 
    for i in range(len(arr)):
        if i < len(arr)-1:
            print(arr[i], end=" ")
        else:
            print(arr[i])

else:
    print("mustahil")