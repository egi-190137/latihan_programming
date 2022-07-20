nTes = int(input())

mTiapTes = []
namaPeserta = []
poinPeserta = []
for _ in range(nTes):
    n, m = [ int(x) for x in input().split() ]
    namaPeserta.append(input())
    mTiapTes.append(m)
    temp = {}
    for i in range(n):
        peserta = [ x for x in input().split() ]
        temp[ peserta[0] ] = [ int(peserta[i]) for i in range(1, len(peserta)) ]
    
    poinPeserta.append(temp)

for i in range(nTes):
    keyPoin = list(poinPeserta[i].keys())
    for j in range(mTiapTes[i]):
        terbesar = j
        for k in range(j+1, len(keyPoin)):
            if poinPeserta[i][keyPoin[terbesar]][2] < poinPeserta[i][keyPoin[k]][2]:
                terbesar = k
            elif poinPeserta[i][keyPoin[terbesar]][2] == poinPeserta[i][keyPoin[k]][2]:
                if poinPeserta[i][keyPoin[terbesar]][1] <  poinPeserta[i][keyPoin[k]][1]:
                    terbesar = k
                elif poinPeserta[i][keyPoin[terbesar]][1] ==  poinPeserta[i][keyPoin[k]][1]:
                    if poinPeserta[i][keyPoin[terbesar]][0] < poinPeserta[i][keyPoin[k]][0]:
                        terbesar = k

        [keyPoin[j], keyPoin[terbesar]] = [keyPoin[terbesar], keyPoin[j]]
    
    if namaPeserta[i] in keyPoin[:mTiapTes[i]]:
        print("YA")
    else:
        print("TIDAK")