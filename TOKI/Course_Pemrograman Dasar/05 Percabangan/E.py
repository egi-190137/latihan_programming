n = int(input())

if n >= 10000:
    print("puluhribuan")
elif n >= 1000:
    print("ribuan")
elif n >= 100:
    print("ratusan")
elif n >= 10:
    print("puluhan")
elif n >= 1:
    print("satuan")