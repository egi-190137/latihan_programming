n = int(input())

array = [ int(x) for x in input().split() ]

terbesar = array[0]
terkecil = array[0]
for i in range(1, len(array)):
    if array[i] > terbesar:
        terbesar = array[i]
    elif array[i] < terkecil:
        terkecil = array[i]

print(f'{terbesar} {terkecil}')
