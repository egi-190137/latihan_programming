arr = []

for i in range(3):
    arr.append( int(input()) )

idxTerkecil = 0
for i in range(1, 3):
    if arr[i] < arr[idxTerkecil]:
        [ arr[idxTerkecil], arr[i] ] = [ arr[i], arr[idxTerkecil] ]

if arr[1] < arr[2]:
    [ arr[1], arr[2] ] = [ arr[2], arr[1] ]

for a in arr:
    print(a)
