def top_3_words(text):
    char = "abcdefghijklmnopqrstuvwxyz'"
    temp = text.split(" ")
    f = {}
    for word in temp:
        if word == '':
            isWord = False
        else:
            isWord = True
            for ch in word:
                if ch not in char:
                    isWord = False
                    break
        if isWord:
            f[word] = 0 if word not in f.keys() else f[word] + 1
    
    f = sorted(f.items(), key=lambda x: x[1], reverse=True)
    hasil = []
    i = 0
    while (i < 3 and i < len(f)):
        hasil.append(f[i][0])
        i += 1
    return hasil

print(top_3_words("a a a  b  c c  d d d d  e e e e e"))
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])

