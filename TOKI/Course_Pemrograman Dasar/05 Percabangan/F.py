n = float(input())

if n%1 == 0:
    print(f'{int(n)} {int(n)}')
elif n < 0:
    print(f'{int(n) - 1} {int(n)}')
else:
    print(f'{int(n)} {int(n) + 1}')