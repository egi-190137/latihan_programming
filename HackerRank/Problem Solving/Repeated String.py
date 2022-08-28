def repeatedString(s, n):
    count_a = 0
    for ch in s:
        if ch == 'a':
            count_a += 1
    
    count_a *= (n // len(s))
    for i in range(n % len(s)):
        if s[i] == 'a':
            count_a += 1
    
    return count_a


if __name__ == '__main__':
    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    print(result)