def viralAdvertising(n):
    shared = 5
    cumuative = 0 
    for i in range(n):
        cumuative += shared // 2
        shared = shared // 2 * 3
    
    return cumuative

if __name__ == '__main__':
    n = int(input().strip())

    result = viralAdvertising(n)

    print(result)