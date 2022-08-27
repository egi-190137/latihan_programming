def main():
    test_cases = int(input())
    for test_case in range(1, test_cases + 1):
        N, R, C, Sr, Sc = map(int, input().split())
        instructions = input()

        final_r, final_c = end_position(N, R, C, Sr, Sc, instructions)
        print(f'Case #{test_case}: {final_r} {final_c}')

def end_position(N, R, C, Sr, Sc, instructions):
    coordinat = [(Sr, Sc)]
    movement = {'N':(-1, 0), 'S':(1, 0), 'E':(0, 1), 'W':(0, -1)}
    for instruct in instructions:
        Sr = coordinat[-1][0] 
        Sc = coordinat[-1][1]
        while True:
            Sr += movement[instruct][0]
            Sc += movement[instruct][1]
            if (Sr, Sc) not in coordinat:
                coordinat.append((Sr, Sc))
                break

    return coordinat[-1]

if __name__ == '__main__':
    main()
