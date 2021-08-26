def is_triangular(t):
    n = 1
    while True:
        triangular = n * (n + 1) / 2
        if triangular == t: 
            return True
        elif triangular > t:
            return False
        n += 1

print(is_triangular(1), True)
print(is_triangular(3), True)
print(is_triangular(6), True)
print(is_triangular(10), True)
print(is_triangular(15), True)
print(is_triangular(21), True)
print(is_triangular(28), True)