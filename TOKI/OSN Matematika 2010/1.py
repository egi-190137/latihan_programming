inputKalimat = input()
kalimat = "halo dunia"

hitung = 0
for i in range(len(inputKalimat)):
    if kalimat[i]==inputKalimat[i].lower():
        hitung+=1

print(hitung)
