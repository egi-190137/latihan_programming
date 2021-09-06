n = input()

yes = False
for c in n:
    if c=="0":
        yes = True
        break

print("YES" if yes else "NO") 