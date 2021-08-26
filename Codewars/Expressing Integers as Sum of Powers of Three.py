def as_sum_of_powers_of_3(n):
    num = 0
    for i in range(-1, 2):
        num = i * 1
        if num == n:
            break
        for j in range(-1, 2):
            
            if j * 3 == n:
                break
            for k in range(-1, 2):
                if k * 9 == n:
                    break
                for l in range(-1, 2):
                    if l * 27 ==