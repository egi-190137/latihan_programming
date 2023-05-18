# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input().strip())

arr1 = set(map(int, input().strip().split()))

n = int(input().strip())

arr2 = set(map(int, input().strip().split()))

result = list(arr1.difference(arr2)) + list(arr2.difference(arr1))

for num in sorted(result):
    print(num)