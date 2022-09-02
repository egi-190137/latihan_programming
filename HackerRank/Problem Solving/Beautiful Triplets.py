def beautifulTriplets(d, arr):
    count = 0
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            if arr[j] - arr[i] < d:
                continue
            if arr[j] - arr[i] > d:
                break
            for k in range(j+1, len(arr)):
                if arr[k] - arr[j] < d:
                    continue
                if arr[k] - arr[j] > d:
                    break
                count += 1
    
    return count

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    print(result)