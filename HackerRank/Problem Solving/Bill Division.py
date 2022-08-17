def bonAppetit(bill, k, b):
    bill.pop(k)
    b_charged = sum(bill) / 2
    if b_charged % 1 == 0:
        b_charged = int(b_charged)
    print("Bon Appetit" if b_charged == b else (b - b_charged))

if __name__ == '__main__':
    [n, k] = [ int(x) for x in input().rstrip().split() ]

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)