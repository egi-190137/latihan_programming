n = int(input())

hasil = []
for i in range(n):
    temp = input()
    hasil.append(int(temp[::-1]))

for h in hasil:
    print(h)