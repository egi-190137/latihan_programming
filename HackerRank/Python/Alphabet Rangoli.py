# Size 5
# e-d-c-b-a-b-c-d-e

# 3 => 9
# 5 => 17
# 10 => 37
# Rumus length = (size - 1) * 2 - 1

def rangoli(length, max):
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    temp = alpha[:max][:-length-1:-1] + alpha[:max][max-length+1:]
    return '-'.join(list(temp))

def print_rangoli(size):
    len_rows = ((size-1) * 4) + 1
    for i in range(1, size+1):
        temp = rangoli(i, size)
        padding_width = (len_rows - len(temp)) // 2
        print("-"*padding_width + temp + "-"*padding_width)

    for i in range(size-1, 0, -1):
        temp = rangoli(i, size)
        padding_width = (len_rows - len(temp)) // 2
        print("-"*padding_width + temp + "-"*padding_width)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)