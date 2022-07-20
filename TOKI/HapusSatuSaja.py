a = input()
b = input()

bisa = False
for i in range(len(a)):
    if a[:i]+a[i+1:] == b:
        bisa = True

if bisa:
    print("Tentu saja bisa!")
else:
    print("Wah, tidak bisa :(")