def reverse_words(text):
    hasil = ""
    temp = ""
    for i in range(len(text)):
        if text[i] != " ":
            temp += text[i]
        elif text[i] == " " or i == len(text) -1 :
            tempArr = []
            for char in temp:
                tempArr.append(char)
            temp = ""
            for j in range(len(tempArr) - 1, -1, -1):
                temp += tempArr[j]
            hasil += temp + text[i]
            temp = ""
    return hasil

print(reverse_words('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god')
print(reverse_words('apple'), 'elppa')
print(reverse_words('a b c d'), 'a b c d')
print(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')                