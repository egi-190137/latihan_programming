def permutationEquation(p):
    temp = p.copy()
    temp = sorted(temp)
    result = []
    for num in temp:
        idx = p.index(num) + 1
        result.append(p.index(idx) + 1)
    
    return result

if __name__ == '__main__':
    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    print('\n'.join(map(str, result)))