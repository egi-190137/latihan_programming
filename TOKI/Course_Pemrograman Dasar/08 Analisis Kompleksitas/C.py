import math

def cekPrima(n):
    if n <= 2:
        return "YA"
    else:
        hitung = 0
        for i in range(2, n//2 + 1):
            if hitung > 2:
                break
            if n%i == 0:
                hitung += 1

        return "YA" if (hitung <= 2) else "BUKAN"

n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

for angka in array:
    print(cekPrima(angka))


# for hasil in array:
#     print("YA" if hasil else "BUKAN")
