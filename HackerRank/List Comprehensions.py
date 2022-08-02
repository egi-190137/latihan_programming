def list_comprehension(x, y, z, n):
    output = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    output.append([i, j, k])
    return output
