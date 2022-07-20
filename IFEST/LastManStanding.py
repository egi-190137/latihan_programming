[n, m] = list(map(int, input().split()))

nomerOrang = [ i for i in range(1, n+1)]

m -= 1
idx = m
while len(nomerOrang) > 1:
    # Menghindari idx melebihi jangkauan
    while idx >= len(nomerOrang):
        idx -= len(nomerOrang)

    # Menghapus anggota pada list
    nomerOrang.pop(idx)
    # Cek apakah orang tereliminasi adalah orang terakhir atau tidak
    if idx == len(nomerOrang):
        idx = 0
    else:
        idx += m

print(nomerOrang[0])