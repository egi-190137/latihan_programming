matriks = []
for i in range(3):
    temp = [ x for x in input().split() ]
    matriks.append(temp)

temp = matriks[0][1]
matriks[0][1] = matriks[1][0]
matriks[1][0] = temp

temp = matriks[0][2]
matriks[0][2] = matriks[2][0]
matriks[2][0] = temp

temp = matriks[1][2]
matriks[1][2] = matriks[2][1]
matriks[2][1] = temp

for baris in matriks:
    print(" ".join(baris))