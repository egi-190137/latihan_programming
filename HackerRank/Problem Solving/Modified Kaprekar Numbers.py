import math

def kaprekarNumbers(p, q):
    result = []
    for i in range(p, q+1):
        square = i**2
        d = len(str(square)) // 2

        r = square % 10**d
        l = (square - r) // 10**d
        if r == 0 and i > 1:
            continue
        # l = square[:int(math.ceil(len(square)/2))]
        # r = square[int(math.ceil(len(square)/2)):]
        if l+r == i:
            result.append(str(i))

    if result == []:
        print("INVALID RANGE")
    else:
        print(" ".join(result))

# def kaprekarNumbers(p, q):
#     result = []
#     for i in range(p, q):
#         square = str(i**2)
#         l = square[:int(math.ceil(len(square)/2))]
#         r = square[int(math.ceil(len(square)/2)):]
#         if r == '':
#             r = 0
#         if int(l)+int(r) == i:
#             result.append(str(i))

#     if result == []:
#         print("INVALID RANGE")
#     else:
#         print(" ".join(result))


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
# print(square)
        # print(len(square))
        # print(int(math.ceil(len(square)/2)))
        # print()