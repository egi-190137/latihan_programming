def jumpingOnClouds(c):
    idx = 0
    count = 0
    while True:
        if idx+2 >= len(c):
            idx += 1
        elif c[idx+2] == 1:
            idx += 1
        else:
            idx += 2

        if idx >= len(c):
            break
        count += 1
    
    return count

if __name__ == '__main__':
    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)