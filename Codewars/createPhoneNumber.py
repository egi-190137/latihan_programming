def create_phone_number(n):
    result = '('
    for i in range(0, 3):
        result += str(n[i])
    
    result += ') '

    for i in range(3, 6):
        result += str(n[i])
    
    result += '-'
    for i in range(6, len(n)):
        result += str(n[i])
    
    return result

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))
print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))