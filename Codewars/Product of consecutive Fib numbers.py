def productFib(prod):
    arr = [0, 1]
    while arr[len(arr) - 1] * arr[len(arr) - 2] < prod:
        arr.append(arr[len(arr) - 1] + arr[len(arr) -2])
    return [arr[len(arr) - 2], arr[len(arr) - 1], (arr[len(arr) - 1] * arr[len(arr) - 2] == prod)]

def productFib(prod):
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]

print(productFib(4895))
