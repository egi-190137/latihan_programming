def getMoneySpent(keyboards, drives, b):
    total = []
    for keyboard in keyboards:
        for drive in drives:
            total.append(keyboard + drive)
    
    total = sorted(total)

    idx = len(total) - 1
    while idx >= 0 and total[idx] > b:
        idx -= 1
    
    if total[idx] > b:
        return -1
    else:
        return total[idx] 

if __name__ == '__main__':
    bnm = input().split()

    b = int(bnm[0])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(moneySpent)