n = int(input())

char = "abcdefghijklmnopqrstuvwxyz"
kalimat = []
for _ in range(n):
    kalimat.append(input())

for k in kalimat:
    k.split("`")
    for i in range(1, len(k) - 1, 2):
        temp = ""
        for j in range(len(k[i])):
            if k[i][j].lower() in char:
                ch = char[len(char) - char.index(k[i][j].lower()) - 1]
                if k[i][j].isUpper():
                    ch = ch.upper()
                temp += ch
        k[i] = temp
    "`".join(k)
print(kalimat)
