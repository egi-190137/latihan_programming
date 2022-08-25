def arrayManipulation(n, queries):
    array = [ 0 for _ in range(n) ]
    for query in queries:
        for i in range(query[0]-1, query[1]):
            array[i] += query[2]
    
    return max(array)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)