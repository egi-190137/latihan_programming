import math

def squares(a, b):
    count = 0
    for i in range(a, b+1):
        if math.sqrt(i) % 1 == 0:
            count += 1
            angka = math.sqrt(i) + 1
            break
    
    if count > 0:
        while math.pow(angka, 2) <= b:
            count += 1
            angka += 1

    return count

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        print(result)