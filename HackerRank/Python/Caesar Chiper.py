def caesarCipher(s, k):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in range(len(s)):
        if s[i].lower() not in alpha:
            result += s[i]
            continue

        char = alpha[ (alpha.index(s[i].lower())+k) % len(alpha) ]
        if s[i].isupper():
            char = char.upper()
        result += char
    return result


if __name__ == '__main__':
    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)
