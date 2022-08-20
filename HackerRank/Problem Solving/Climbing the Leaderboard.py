def climbingLeaderboard(ranked, player):
    result = []
    temp = []
    for num in ranked:
        if num not in temp:
            temp.append(num)
    
    ranked = temp
    idx = len(ranked)
    for i in range(len(player)):
        while idx > 0 and player[i] >= ranked[idx-1]:
            idx -= 1
        
        result.append(idx+1)
    return result
        

if __name__ == '__main__':
    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print('\n'.join(map(str, result)))