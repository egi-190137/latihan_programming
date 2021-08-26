def solution(string,markers):
    string = string.split("\n")
    hasil = []
    for kalimat in string:
        temp = ""
        for ch in kalimat:
            if ch in markers:
                break
            temp += ch
        while len(temp) > 0 and temp[len(temp) - 1] == " ":
            temp = temp[:-1]
        hasil.append(temp)
    return "\n".join(hasil)

result = solution("", ["#", "!"])
print(result)