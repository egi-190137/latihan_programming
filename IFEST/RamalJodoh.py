n = int(input())

nama = []
for _ in range(n):
    temp = input().split()
    if len(temp[1]) < len(temp[0]):
        [temp[1], temp[0]] = [temp[0], temp[1]]
    nama.append(temp)

for i in range(len(nama)):
    idx = []
    for ch in nama[i][0]:
        if idx == []:
            iAwal = 0
        else:
            iAwal = idx[len(idx) - 1] + 1
        for j in range(iAwal, len(nama[i][1])):
            if nama[i][1][j] == ch:
                idx.append(j)
                break
                
    if len(idx) == len(nama[i][0]):
        print("BOLEH")
    else:
        print("JANGAN")