def coloring_game(n):
    sequence = [ True for _ in range(n) ]
    bot = True
    count_bot = 0
    for i in range(0, len(sequence), 2):    
        sequence[i] = False
        if bot:
            bot = False
            count_bot += 1
        else:
            bot = True
    return count_bot

t = int(input())
arr = []
for _ in range(t):
    arr.append(int(input()))

for i, item in enumerate(arr):
    print(f"Case #{i+1}: {coloring_game(item)}")