panjang, bintang = [ int(x) for x in input().split() ]

array = []
for i in range(1, panjang + 1):
    array.append("*" if i%bintang == 0 else str(i))

print(" ".join(array))