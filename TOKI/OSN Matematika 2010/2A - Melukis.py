# mengambil nilai  w dan h
angkaStr = input().split(" ")
w, h = int(angkaStr[0]), int(angkaStr[1])

# membuat matriks
matriks = [ [0 for i in range(w) ] for i in range(h) ]

n = int(input())
for i in range(n):
    # format input "a b c d k"
    inputString = input().split(" ")
    intAngka = [ int(i) for i in inputString ]
    [a, b, c, d, k] = intAngka

    for j in range(b-1, d):
        for l in range(a-1, c):
            matriks[j][l] = k

for i in range(len(matriks)):
    output = ""
    for j in range(len(matriks[i])):
        output += str(matriks[i][j])
    print(output)
