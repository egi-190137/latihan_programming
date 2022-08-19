def pageCount(n, p):
    return min([p // 2, (n-p + (1 if n%2 == 0 else 0) ) // 2])

if __name__ == '__main__':
    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(result)