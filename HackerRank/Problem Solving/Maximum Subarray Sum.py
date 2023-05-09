# def maximumSum(a, m):
#     max_result = 0
#     for i in range(1, len(a)+1):
#         first_sum = sum(a[0:i])
#         if (first_sum % m) > max_result:
#             max_result = (first_sum % m)

#         for j in range(1, len(a)-i+1):
#             first_sum = first_sum + a[j+i-1] - a[j-1]
#             if (first_sum % m) > max_result:
#                 max_result = first_sum % m
    
#     return max_result

def maximumSum(a, m):
    for i in range(len(a)):
        a[i] %= m
    
    print(a)
    max_result = 0
    for i in range(1, len(a)+1):
        first_mod = sum(a[0:i]) % m
        if first_mod > max_result:
            max_result = first_mod
        
        if max_result == m-1:
            return max_result

        for j in range(1, len(a)-i+1):
            first_mod = ( first_mod + a[j+i-1] - a[j-1] ) % m
            if first_mod > max_result:
                max_result = first_mod

            if max_result == m-1:
                return max_result
    
    return max_result


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        print(result)
