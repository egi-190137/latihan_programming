def swap_case(s):
    result = ""
    for ch in s:
        if ch.isupper():
            result += ch.lower()
        elif ch.islower():
            result += ch.upper()
        else:
            result += ch
    
    return result
