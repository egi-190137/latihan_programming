def cutTheSticks(arr):
    result = []
    while len(arr) > 0:
        result.append(len(arr))
        
        minimum = min(arr)
        idx = 0
        while idx < len(arr):
            if minimum == arr[idx]:
                arr.pop(idx)
                idx -=1
            else:
                arr[idx] -= minimum
            idx+=1

    return result

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    print('\n'.join(map(str, result)))