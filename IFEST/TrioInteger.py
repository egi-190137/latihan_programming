a = list(map(int, input().split()))

for i in range(len(a) - 2):
    for j in range(i+1, len(a) - 1):
        for k in range(j+1, len(a)):
            if a[i]+a[j] == a[k] or a[i]+a[k] == a[j] or a[j]+a[k] == a[i]:
                print(a[i], a[j], a[k])