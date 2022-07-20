a, b, k, x = [ int(x) for x in input().split() ]

def f(x):
    return abs(a*x + b)

hasil = f(x)
for _ in range(k-1):
    hasil = f(hasil)

print(hasil)