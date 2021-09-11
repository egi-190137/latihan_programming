n = int(input())

waktu = (3600, 60, 1)
for w in waktu:
    print(n//w)
    n %= w