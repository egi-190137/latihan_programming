def countingValleys(steps, path):
    height = 0
    count = 0
    for ch in path:
        if ch == "U":
            height += 1
        else:
            height -= 1
            if height == -1:
                count += 1
    
    return count

if __name__ == '__main__':
    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result)