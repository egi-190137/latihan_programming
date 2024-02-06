def solution(s):
    hasil = ""
    for ch in s:
        if ch.upper() == ch:
            hasil += " "
        hasil += ch
    return hasil


print(solution("breakCamelCase"))
print("breakCamelCase")
