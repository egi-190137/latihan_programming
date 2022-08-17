def getTotalX(a, b):
    factor = []
    a = sorted(a)
    b = sorted(b)
    temp = a[-1]
    while temp <= b[0]:
        isFactor = True
        for num in a:
            if temp % num != 0:
                isFactor = False
                break

        if isFactor:
            factor.append(temp)
        temp += a[-1]

    idx = 0
    while idx < len(factor):
        for num in b:
            if num % factor[idx] != 0:
                factor.pop(idx)
                idx -= 1
                break
        
        idx += 1
    
    return len(factor)

if __name__ == '__main__':

    [n, m] = [ int(x) for x in input().split() ]

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    print(getTotalX(arr, brr))