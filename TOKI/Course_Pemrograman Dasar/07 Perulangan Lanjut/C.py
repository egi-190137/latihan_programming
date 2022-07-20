n = int(input())

angka = 0
for i in range(n):
    for j in range(i+1):
        print(angka, end="")
        if angka == 9:
            angka = 0
        else:
            angka+=1
    print("")