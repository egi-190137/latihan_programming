def cavityMap(grid):
    grid = [ [ num for num in row ] for row in grid]
    num_grid = [ [ int(num) for num in row ] for row in grid]
    
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[i]) - 1):
            if num_grid[i][j] > num_grid[i-1][j] and \
                    num_grid[i][j] > num_grid[i+1][j] and \
                    num_grid[i][j] > num_grid[i][j-1] and \
                    num_grid[i][j] > num_grid[i][j+1]:
                
                grid[i][j] = "X"
    return [ "".join(row) for row in grid ]

if __name__ == '__main__':
    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    print('\n'.join(result))