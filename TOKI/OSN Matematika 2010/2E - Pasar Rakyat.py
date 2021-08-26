n = int(input())

listAngka = []
for i in range(n):
    listAngka.append(int(input()))

hasil = max(listAngka)
while True:
    isKPK = True
    for angka in listAngka:
        if hasil % angka > 0:
            isKPK = False
            break
    if isKPK:
        break
    else:
        hasil += 1

print(hasil)
