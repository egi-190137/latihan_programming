import math

def encryption(s):
    s = ''.join(s.split())
    rows = math.sqrt(len(s))

    columns = math.ceil(rows)
    rows = math.floor(rows)
    if columns * rows < len(s):
        rows += 1
        
    result = ''
    for i in range(columns):
        idx = i
        for j in range(rows):
            if idx < len(s):
                result += s[idx]
                idx += columns
        result += ' '
    
    return result

if __name__ == '__main__':
    s = input()

    result = encryption(s)

    print(result)