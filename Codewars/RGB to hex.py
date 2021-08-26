def rgb(r, g, b):
    listRGB = [r, g, b]
    listHex = []
    hexa = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for num in listRGB:
        hasil = []
        if num < 0:
            hasil = ["0", "0"]
        elif num > 255:
            hasil = ["F", "F"]
        else:
            while num > 0:
                if num < 16:
                    hasil.append(hexa[num - 1])
                    num = 0
                else:
                    hasil.append(hexa[(num % 16) - 1])
                    num = num // 16
        hasil.sort()
        listHex.append(''.join(hasil))
    return ''.join(listHex)

print(rgb(-20, 275, 125))