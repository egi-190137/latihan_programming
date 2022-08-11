if __name__ == '__main__':
    s = input()
    
    output = [ False for _ in range(5) ]
    for ch in s:
        if ch.isalnum():
            output[0] = True
        if ch.isalpha():
            output[1] = True
        if ch.isdigit():
            output[2] = True
        if ch.islower():
            output[3] = True
        if ch.isupper():
            output[4] = True

for out in output:
    print(out)
