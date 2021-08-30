password = input()

syarat = [ len(password) >= 8, False, False, False, False ]

# syarat[0] : >=8 karakter
# syarat[1] : ada huruf besar
# syarat[2] : ada huruf kecil
# syarat[3] : ada angka
# syarat[4] : ada karakter khusus 
abjad = "abcdefghijklmnopqrstuvwxyz"
angka = "1234567890"

jumlahAbjad = 0
for ch in password:
    if ch in abjad.upper():
        syarat[1] = True
        jumlahAbjad += 1
    elif ch in abjad:
        syarat[2] = True
        jumlahAbjad += 1
    elif ch in angka:
        syarat[3] = True
    else:
        syarat[4] = True

if syarat==[1,1,1,1,1]:
    print("Kuat")
elif jumlahAbjad > 12:
    print("AgakKuat")
else:
    print("Lemah")
