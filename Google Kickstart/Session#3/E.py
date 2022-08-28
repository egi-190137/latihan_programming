from math import pow

def count_pairs(a, b, n, k):
    pairs = 0
    for i in range(1, n+1):
        i_pangkat_a = pow(i, a)
        for j in range(1, n+1):
            if i != j:
                if (i_pangkat_a + pow(j, b)) % k == 0:
                    pairs += 1
    return pairs

if __name__ == '__main__':
    # Read number of test cases
    num_cases = int(input())

    for tc in range(1, num_cases + 1):
        a, b, n, k = map(int, input().split())

        print("Case #%d: %d" % (tc, count_pairs(a, b, n, k)))
