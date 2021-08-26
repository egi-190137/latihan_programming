def ips_between(start, end):
    start = start.split(".")
    end = end.split(".")
    selisih = 0
    for i in range(len(start) - 1, -1, -1):
        selisih += 256 ** (len(start) - i - 1) * ( int(end[i]) - int(start[i]) )
    return selisih

print(ips_between("20.0.0.10", "20.0.1.0"), 246)
print(ips_between("10.0.0.0", "10.0.0.50"), 50)
print(ips_between("67.166.20.111","255.255.255.255"), 3160009616)
