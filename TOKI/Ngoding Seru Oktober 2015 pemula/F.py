ukuranBaju = [
    [10, 40, 90],
    [14, 60, 120],
    [18, 80, 180],
    [25, 100, 220]
]

# Keterangan
# [0] => S; [1] => M; [2] => L; [3] => X
# [i][0] => Bahu; [i][1] => Panjang; [i][2] => UkuranLingkar

ukuran = ("S", "M", "L", "X")
ukuranKei = list(map(int, input().split()))

for i in range(len(ukuranBaju)):
    muat = True
    for j in range(len(ukuranBaju[i])):
        if ukuranBaju[i][j] < ukuranKei[j]:
            muat = False
            break
    
    if muat:
        print(ukuran[i])
        break

if not muat:
    print("X") 
