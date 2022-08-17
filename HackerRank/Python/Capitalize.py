def solve(s):
    arr = []
    temp = ""
    for ch in s:
        if temp != "":
            if ch != " " and temp[-1] == " " or ch == " " and temp[-1] != " ":
                arr.append(temp)
                temp = ch
            else:
                temp += ch
        else:
            temp += ch
    arr.append(temp)
    return "".join(map(lambda x: x.capitalize(), arr))

if __name__ == '__main__':
    s = input()

    print(solve(s))
