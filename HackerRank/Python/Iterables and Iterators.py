from itertools import combinations

n = int(input())
chars = "".join(input().split())
k = int(input())

s = list(combinations(chars, k))

count_s = 0
for item in s:
    if 'a' in item:
        count_s += 1

print(count_s / len(s)) 