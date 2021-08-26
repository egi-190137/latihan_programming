def mix(s1, s2):
    numS1 = {}
    numS2 = {}
    for ch in s1:
        if ch.isalpha():
            ch = ch.lower()
            if ch not in numS1.keys():
                numS1[ch] = 1
            else:
                numS1[ch] += 1

    for ch in s2:
        if ch.isalpha():
            ch = ch.lower()
            if ch not in numS2.keys():
                numS2[ch] = 1
            else:
                numS2[ch] += 1
    
    hasil = []
    for c in sorted numS1.keys():
        if c in numS2.keys():
            if numS1[c] == numS2[c]:
                temp = "=:" + c * numS1[c]
            elif numS1[c] > numS2[c]:
                temp = ("1:" + c * numS1[c])
            else:
                temp = "2:" + c * numS2[c] 
            hasil.append(temp)

    print(numS1)
    print(numS2)
    return "/".join(hasil)


s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
print(mix(s1,s2))
print("1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss")