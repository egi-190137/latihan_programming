import random
import sys

inputRange = input().split(" ")

a, b = int(inputRange[0]), int(inputRange[1])


while a <= b:
    angka = (a+b) // 2
    print(angka)
    sys.stdout.flush()
    inputSalahBenar = input()
    if inputSalahBenar == "selamat":
        break
    elif inputSalahBenar == "terlalu kecil":
        a = angka + 1
    else:
        b = angka - 1
