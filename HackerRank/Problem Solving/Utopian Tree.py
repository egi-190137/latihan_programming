def utopianTree(n):
    # height = [1, 2, 3, 6, 7, 14]
    # return height[n]
    if n == 0:
        return 1
    elif n % 2 == 0:
        return utopianTree(n-1) + 1
    else:
        return utopianTree(n-1) * 2

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        print(result)