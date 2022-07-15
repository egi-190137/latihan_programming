uang = int(input())

listPecahan = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]

idx = len(listPecahan) - 1

while uang > 0:
    bagi = uang // listPecahan[idx]
    if bagi > 0:
        print("{} {}".format(listPecahan[idx], bagi))
    uang = uang % listPecahan[idx]
    idx -= 1
