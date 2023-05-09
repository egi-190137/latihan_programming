def lonelyinteger(a):
    a = sorted(a)
    unique_num = a[0]
    is_unique = True
    for i in range(1, len(a)):
        if a[i] == unique_num:
            is_unique = False
        elif not is_unique:
            if a[i] != unique_num:
                unique_num = a[i]
                is_unique = True
    return unique_num

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    print(result)
