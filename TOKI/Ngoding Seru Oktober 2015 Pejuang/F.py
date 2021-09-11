[n, h] = list(map( int, input().split() ))
tinggi = list(map( int, input().split() ))

palingTinggi = 0
for t in tinggi:
    if palingTinggi < t:
        palingTinggi = t

h -= palingTinggi
palingRendah = palingTinggi

for t in tinggi:
    if t >= h and t < palingRendah:
        palingRendah = t

print(palingRendah + palingTinggi)