def mixed_fraction(s):
    pembilang = int(s.split("/")[0])
    penyebut = int(s.split("/")[1])
    hasil = "" if pembilang // penyebut == 0 else "{}".format(pembilang // penyebut)
    pembilang %= penyebut
    if pembilang == 0:
        return hasil
    else:
        for i in range(pembilang, 2-1, -1):
            if pembilang % i == 0 and penyebut % i == 0:
                pembilang //= i
                penyebut //= i
                break
        return hasil + " {}/{}".format(pembilang, penyebut)

print(mixed_fraction('42/9'))
