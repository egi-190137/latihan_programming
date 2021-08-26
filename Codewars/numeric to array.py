def numToArray(angka):
    hasil = []
    while (angka > 0):
        hasil.insert(0, angka % 10)
        angka //= 10
    return hasil

print(numToArray(12345678901234567890))