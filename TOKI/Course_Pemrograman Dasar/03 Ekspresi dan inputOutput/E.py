alas, tinggi = [ int(x) for x in input().split() ]

luas = str(0.5 * alas * tinggi).split(".")

while len(luas[1]) < 2:
    luas[1] += "0"

print(".".join(luas))