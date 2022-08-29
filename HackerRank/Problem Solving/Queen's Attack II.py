def queensAttack(n, k, r_q, c_q, obstacles):
    directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    count = 0
    for direction in directions:
        temp_r = r_q
        temp_c = c_q
        while True:
            temp_r += direction[0]
            temp_c += direction[1]
            if temp_c > n or temp_c < 1:
                break
            if temp_r > n or temp_r < 1:
                break
            if [temp_r, temp_c] in obstacles:
                break
            count += 1
    
    return count

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(result)