def check_consecutive(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True

    return False

def alternate(s):
    chars = list(set(s))

    max_result = 0
    for i in range(len(chars)-1):
        for j in range(i+1, len(chars)):
            string_result = ""
            for c in s:
                if c in ( chars[i], chars[j] ):
                    string_result += c
            
            if not check_consecutive(string_result):
                if len(string_result) > max_result:
                    max_result = len(string_result)

    return max_result


if __name__ == '__main__':

    s = input()

    result = alternate(s)

    print(result)
