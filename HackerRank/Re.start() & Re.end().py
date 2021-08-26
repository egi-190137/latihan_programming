s = input()
k = input()

for i in range(len(s) - len(k) + 1):
    if s[i:i+len(k)] == k:
        print((i, i + len(k) - 1))