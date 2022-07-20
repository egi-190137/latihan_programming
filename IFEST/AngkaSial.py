n = int(input())

noKamar = []
for _ in range(n):
    noKamar.append(list(map(int, input().split())))

for no in noKamar:
    temp = 0
    for i in range(no[0], no[1] + 1):
        if i%10 == 3 or i%10 == 4:
            temp += 1
    print(temp)