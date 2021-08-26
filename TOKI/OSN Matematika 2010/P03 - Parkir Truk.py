aBC = input().split(" ")

harga = [ int(a) for a in aBC ]

waktu = [[], []]
for i in range(3):
    xy = input().split(" ")
    waktu[0].append( int(xy[0]) )
    waktu[1].append( int(xy[1]) )

for i in range(2):
    for j in range(2, 0, -1):
        for k in range(j):
            if waktu[i][k] > waktu[i][k+1]:
                [waktu[i][k], waktu[i][k+1]] = [waktu[i][k+1], waktu[i][k]]

total = 0
for i in range(3):
    if i < 2:
        selisihWaktu = waktu[0][i+1] - waktu[0][i] + (waktu[1][len(waktu[1]) - i - 1] - waktu[1][len(waktu[1]) - i - 2])
    else:
        selisihWaktu = waktu[1][len(waktu[0]) - i - 1] - waktu[0][i]
    total += selisihWaktu * harga[i] * (i+1)

print(total)