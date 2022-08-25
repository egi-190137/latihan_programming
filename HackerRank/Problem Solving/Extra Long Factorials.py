def extraLongFactorials(n):
    hasil = 1
    for i in range(2, n+1):
        hasil *= i
    
    return hasil

if __name__ == '__main__':
    n = int(input().strip())

    print(extraLongFactorials(n))
