angka = int(input(""))

idx = 1
a = 0
b = 1
c = 0
while c < angka:
    if idx == 1:
        c = 0
    if idx == 2:
        c = 1
    else:
        c = a+b
        a = b
        b = c
    idx += 1

if c == angka:
    print(idx)
else:
    print(0)
