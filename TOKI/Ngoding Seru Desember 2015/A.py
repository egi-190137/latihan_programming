arr = []

for i in range(3):
    arr.append( int(input()) )

total = 0
lolos = True
for a in arr:
    if a < 50:
        lolos = False
    total += a

if total < 200:
    lolos = lolos and False

print("Lolos" if lolos else "Tidak Lolos")