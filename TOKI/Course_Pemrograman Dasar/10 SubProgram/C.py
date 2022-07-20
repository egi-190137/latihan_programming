def reverse(x):
    temp = x
    ret  = 0

    while temp > 0:
        ret  = (ret * 10) + (temp % 10)
        temp = temp // 10

    return ret

a, b = [ reverse(int(x)) for x in input().split() ]

c = reverse(a + b)
print(c)