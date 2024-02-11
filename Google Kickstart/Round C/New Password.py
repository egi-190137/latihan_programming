def checkAlpha(password, upper):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    if upper:
        alpha = alpha.upper()
    for a in alpha:
        if a in password:
            return True

    return False


def checkDigit(password):
    digit = "0123456789"
    for a in digit:
        if a in password:
            return True

    return False


def checkSpesial(password):
    digit = "#", "@", "*", "&"
    for a in digit:
        if a in password:
            return True

    return False


t = int(input())

arr = []
for _ in range(t):
    temp = int(input())
    arr.append(input())


for i in range(len(arr)):
    while True:
        if not checkAlpha(arr[i], True):
            arr[i] += "A"
        if not checkAlpha(arr[i], False):
            arr[i] += "a"
        if not checkDigit(arr[i]):
            arr[i] += "1"
        if not checkSpesial(arr[i]):
            arr[i] += "#"

        if len(arr[i]) < 7:
            arr[i] += "a"
        else:
            break
    print(f"Case #{i+1}: {arr[i]}")
