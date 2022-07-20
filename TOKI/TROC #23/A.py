n = int(input())

total = 1
for i in range(2, n+1):
    if n%i == 0:
        total += 1
    if total > 5:
        break

if total == 5:
    print("YES")
else:
    print("NO")