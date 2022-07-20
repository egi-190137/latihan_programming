from unittest import result


t = int(input())
tests = []
for i in range(t):
    temp = {}
    [ temp['N'], temp['M'] ] = map(int, input().split())
    temp['C'] = map(int, input().split())
    tests.append(temp)

for i in range(t):
    result = sum(tests[i]['C']) % tests[i]['M']
    print(f'Case #{i+1}: {result}')
