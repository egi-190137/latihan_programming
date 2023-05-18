import re

t = int(input())

phone_numbers = list()
for _ in range(t):
    phone_numbers.append(input())
    
for i in range(len(phone_numbers)):
    is_valid = re.match(r'^[7-9]\d{9}$', phone_numbers[i])

    print('YES' if is_valid else 'NO')