[n, m] = [ int(x) for x in input().split(" ") ]
arr = [ int(x) for x in input().split(" ") ]
A = { int(x) for x in input().split(" ") }
B = { int(x) for x in input().split(" ") }

happiness = 0
for i in range(n):
    if arr[i] in A:
        happiness += 1
    if arr[i] in B:
        happiness -= 1

print(happiness)
