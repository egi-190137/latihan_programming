def libraryFine(d1, m1, y1, d2, m2, y2):
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # for i in range(m1-1):
    #     if i == 1 and y1 % 4 == 0:
    #         d1 += 29
    #     else:
    #         d1 += month[i]
    #     print(f"iter {i}")

    # for i in range(m2-1):
    #     if i == 1 and y2 % 4 == 0:
    #         d2 += 29
    #     else:
    #         d2 += month[i]
    #     print(f"iter {i}")


    # print(d1)
    # print(d2)
    # d_difference = d1 - d2 + (y1 - y2) * 365
    return 15 * (d1-d2) + 500 * (m1-m2) + 10000 * (y1-y2)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    print(result)