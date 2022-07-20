x = int(input())

faktor = {}
pembagi = 2
while x > 1:
    if x % pembagi == 0:
        x /= pembagi
        if pembagi in faktor.keys():
            faktor[pembagi] += 1
        else:
            faktor[pembagi] = 1
    else:
        pembagi += 1
    
hasil = []
for key in faktor.keys():
    if faktor[key] == 1:
        hasil.append(str(key))
    else:
        hasil.append(f"{key}^{faktor[key]}")

print(" x ".join(hasil))
