from ctypes import cdll


k = int(input())
c = input()
d = input()

if k % 2 == 0:
    tengah = -1
else:
    tengah = k // 2

for i in range(k):
    temp = ""
    for j in range(k):
        if i == 0 or i == k-1 or j == 0 or j == k-1:
            temp += d
        elif i == tengah and j == tengah:
            temp += "*"
        else:
            temp += c
    print(temp)