def longest(a1, a2):
    temp = a1 + a2
    arrayString = []
    for ch in temp:
        arrayString.append(ch)

    temp = sorted(temp)
    hasil = ""
    for ch in temp:
        if ch not in hasil:
            hasil += ch
    return hasil

a = "abcdefghijklmnopqrstuvwxyz"
print(longest(a, a))
print("abcdefghijklmnopqrstuvwxyz")