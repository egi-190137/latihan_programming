def rangoli(length, max):
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    temp = alpha[:max][:-length+1:-1] + alpha[:max][max-length+1:]
    return '-'.join(list(temp))

def print_rangoli(size):
    for i in range(1, size):
        print(rangoli(i, size))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)