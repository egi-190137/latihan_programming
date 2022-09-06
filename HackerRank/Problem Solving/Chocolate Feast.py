def chocolateFeast(n, c, m):
    count_chocolate = n // c
    wrapper = count_chocolate
    while wrapper >= m:
        count_chocolate += wrapper // m
        wrapper = wrapper % m + wrapper // m
    return count_chocolate

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        print(result)