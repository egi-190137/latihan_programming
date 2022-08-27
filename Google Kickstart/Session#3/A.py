divideCandies = lambda candies, m : sum(candies) % m

t = int(input())

candies = []
m = []
for _ in range(t):
    m.append(int(input().split()[1]))
    candies.append(list(map(int, input().split())))

for i in range(t):
    print(f'Case #{i+1}: {divideCandies(candies[i], m[i])}')