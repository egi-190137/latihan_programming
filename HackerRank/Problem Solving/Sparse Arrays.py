def matchingStrings(strings, queries):
    result = {}
    for s in strings:
        if s in queries:
            if s not in result:
                result[s] = 1
            else:
                result[s] += 1

    output = []
    for q in queries:
        if q in result.keys():
            output.append(result[q])
        else:
            output.append(0)

    return output

if __name__ == '__main__':
    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    print('\n'.join(map(str, res)))