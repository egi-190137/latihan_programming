def catAndMouse(x, y, z):
    distanceA = abs(z-x)
    distanceB = abs(z-y)
    if distanceA == distanceB:
        return 'Mouse C'
    elif distanceA < distanceB:
        return 'Cat A'
    else:
        return 'Cat B'

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result)