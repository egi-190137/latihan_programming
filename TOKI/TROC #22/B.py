n = int(input())
a = 0

hasil = ""
while a < n:
    if a % 3 == 0:
        hasil += "p"
    elif a % 3 == 1:
        hasil += "i"
    else:
        hasil += "e"
    a += 1

print(hasil)