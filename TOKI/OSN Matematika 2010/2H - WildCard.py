wildWord = input().split("*")
n = int(input())

hasil = []
for i in range(n):
    temp = input()
    if wildWord[0] == temp[:len(wildWord[0])] or wildWord[0] == "":
        if wildWord[1] == "" or wildWord[1] == temp[-len(wildWord[1]):]:
            hasil.append(temp)

for kata in hasil:
    print(kata)