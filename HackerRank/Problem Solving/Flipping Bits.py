def flippingBits(n):
    result = 0
    div = 1
    for _ in range(32):
        temp = 0 if n % 2 else 1
        n //= 2
        result += temp*div
        div *= 2
    return result

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        print(result)