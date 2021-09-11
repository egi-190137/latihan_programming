n = int(input())
arr = [ int(x) for x in input().split() ]

q = int(input())
query = []
for i in range(q):
    query.append( [ int(x) for x in input().split() ] )

for que in query:
    if que[0] == 1:
        for i in range(que[1], que[2]):
            arr[i] += que[3]
    else:
        length = 0
        sebelumnyaCantik = False
        for i in range(que[1]+1, que[2]-1):
            if arr[i-1] < arr[i] > arr[i+1] or arr[i-1] > arr[i] < arr[i+1]:
                if not sebelumnyaCantik:
                    length += 3
                    sebelumnyaCantik = True
                else:
                    length += 1
            else:
                sebelumnyaCantik = False
        print(length)