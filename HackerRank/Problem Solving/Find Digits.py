def findDigits(n):
    temp = n
    count = 0
    while temp > 0:
        pembagi = temp % 10
        temp //= 10
        if pembagi > 0 and n % pembagi == 0:
            count += 1
    
    return count

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        print(result)