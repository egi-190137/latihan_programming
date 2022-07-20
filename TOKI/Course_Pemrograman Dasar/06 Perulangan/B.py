n = int(input())

arrayAngka = [ int(x) for x in input().split() ]

total = 0
for angka in arrayAngka:
    total += angka

print(total)