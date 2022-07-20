n = int(input())

array = [ int(x) for x in input().split() ]

banyakMuncul = {}
for angka in array:
    if angka not in banyakMuncul.keys():
        banyakMuncul[angka] = 1
    else:
        banyakMuncul[angka] += 1

tersering = array[0]
for key in banyakMuncul.keys():
    if banyakMuncul[tersering] < banyakMuncul[key]:
        tersering = key
    elif banyakMuncul[tersering] == banyakMuncul[key] and key > tersering:
        tersering = key

print(tersering)
