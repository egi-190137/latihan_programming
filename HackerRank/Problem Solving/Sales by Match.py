def sockMerchant(n, ar):
    num = {}
    for a in ar:
        if a not in num.keys():
            num[a] = 1
        else:
            num[a] += 1
    
    result = 0
    for value in num.values():
        result += value // 2
    
    return result


if __name__ == '__main__':
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(str(result) + '\n')