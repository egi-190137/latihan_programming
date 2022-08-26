def equalizeArray(arr):
    numCount = {}
    for num in arr:
        if num in numCount.keys():
            numCount[num] += 1
        else:
            numCount[num] = 1
    
    return len(arr) - max(numCount.values())

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    print(result)