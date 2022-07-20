import math

def cekPrima(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        y = int(math.sqrt(n))
        test = True
        while y >= 2 and test:
            if n % y == 0:
                test = False
            y -= 1
        return test

    # jumlah = 0
    # for i in range(1, n+1):
    #     if n%i == 0:
    #         jumlah += 1
    
    # return (jumlah == 2)

n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

for angka in array:
    if cekPrima(angka):
        print("YA")
    else:
        print("BUKAN")
