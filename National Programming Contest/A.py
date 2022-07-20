t = int(input())

mDanN = []
for _ in range(t):
    mDanN.append([ int(x) for x in input().split() ])

for i in range(t):
    temp = [ 0 for i in range(mDanN[i][1]) ]
    temp[0] = mDanN[i][0]
    jumlah = 1
    idx = 0
    while idx < len(temp) - 1 and temp[idx] > 1:
        print(temp)
        temp[idx] -= 1
        temp[idx+1] += 1
        print(temp)
        if temp[idx+1] > 1:
            idx += 1
        else:
            while temp[idx] == 1:
                # temp[idx] -= 1
                # temp[idx-1] += 1
                idx -= 1
        # else:
        #     idx += 1
        print(idx)
        jumlah += 1
    print(jumlah)