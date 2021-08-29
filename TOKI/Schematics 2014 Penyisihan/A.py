penghasilan = input().split(" ")

total = 0
for a in penghasilan:
    total += int(a)

# print("Rp " + str(total // 4) + "," + str((total % 4) * 25))
print(f'Rp {total // 4},{"00" if total % 4 == 0 else (total % 4) * 25}')