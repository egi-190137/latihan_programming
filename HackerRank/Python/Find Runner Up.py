def findRunnerUp(arr):
    arr = list(set(arr))
    for i in range(2):
        maxIdx = i
        for j in range(i+1, len(arr)):
            if arr[maxIdx] < arr[j]:
                maxIdx = j
        
        arr[maxIdx], arr[i] = arr[i], arr[maxIdx]
    
    return arr[1]
