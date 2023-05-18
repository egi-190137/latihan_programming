def des2bin(num):
    result = 0
    kali = 1
    while num > 0:
        result += (num%2) * kali
        kali *= 10
        num //= 2
    return result

def xor_operation(a, b):
    a_bin = des2bin(a)
    b_bin = des2bin(b)

    penambah = 1
    result = 0
    while a_bin > 0 or b_bin > 0:
        if (a_bin % 10) != (b_bin % 10):
            result += penambah
        penambah *= 2 
        a_bin //= 10
        b_bin //= 10
    
    return result

def maximizingXor(l, r):
    max_result = 0
    for a in range(l, r+1):
        for b in range(a, r+1):
            if a == b:
                continue

            temp = xor_operation(a, b)
            if max_result < temp:
                max_result = temp

    return max_result

if __name__ == '__main__':
    l = int(input().strip())

    r = int(input().strip())

    print(maximizingXor(l, r))