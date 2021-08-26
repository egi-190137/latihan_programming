angka = int(input("Masukkan angka : "))

paskal = []
for i in range(angka):
    temp = []
    for j in range(i + 1):
        if j == 0 or j == i:
            temp.append(1)
        else:
            temp.append(paskal[len(paskal) - 1][j] + paskal[len(paskal) - 1][j -1])
    paskal.append(temp)

for i in range(len(paskal)):
    for j in range(len(paskal) - j):
        print("  ", end="")
    for j in range(len(paskal[i])):
        print(str(paskal[i][j]), end=" ")
    print("")
print(paskal)
