listBerat = []

temp = []
for i in range(10):
    angka = int(input())
    if angka == 0:
        listBerat.append(temp)
        temp = []
    else:
        temp.append(angka)

listBerat.append(temp)

for i in range(len(listBerat)):
    terbesar = 1
    terkecil = 10000
    for j in range(len(listBerat[i])):
        if terbesar < listBerat[i][j]:
            terbesar = listBerat[i][j]
        if terkecil > listBerat[i][j]:
            terkecil = listBerat[i][j]
    print("{} {}".format(terkecil, terbesar))
