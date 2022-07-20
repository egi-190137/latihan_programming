array = [ int(x) for x in input().split() ]

jarak = 0
if array[0] > array[2]:
    jarak += array[0] - array[2]
else:
    jarak += array[2] - array[0]

if array[1] > array[3]:
    jarak += array[1] - array[3]
else:
    jarak += array[3] - array[1]

print(jarak)