def reverseArray(a):
    return [ a[i] for i in range(len(a)-1, 0-1, -1) ]

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    print(' '.join(map(str, res)))
