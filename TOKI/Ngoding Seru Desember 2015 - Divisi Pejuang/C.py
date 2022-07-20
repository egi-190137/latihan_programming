def getArrWord(word):
    word = word.split(" ")
    word[len(word) - 1] = word[len(word) - 1][:-1]
    result = []
    for i in range(len(word)):
        countLowerCase = 0
        countDigit = 0
        for ch in word[i]:
            if ch.isdigit():
                countDigit += 1
            elif ch.islower():
                countLowerCase += 1
        
        if countDigit >= 1 and countLowerCase >= 3:
            result.append(word[i])
        
    return result

def getLongestWord(arrWord):
    longest = arrWord[0]
    for i in range(1, len(arrWord)):
        if len(longest) < len(arrWord[i]):
            longest = arrWord[i]
    return longest

word = input()

numberWord = getArrWord(word)

if numberWord == []:
    print("NO")
else:
    hasil = getLongestWord(numberWord)

    print(hasil)
    print(len(hasil))