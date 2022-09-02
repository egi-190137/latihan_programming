def angryProfessor(k, a):
    count = 0
    idx = 0
    while idx < len(a) and count < k:
        if a[idx] <= 0:
            count += 1
        idx += 1
    return 'YES' if count < k else 'NO'

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        print(result)