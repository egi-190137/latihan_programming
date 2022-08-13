def count_substring(sub, string):
    count = 0
    for i in range(len(string) - len(sub) + 1):
        if sub == string[i:i+len(sub)]:
            count += 1
    
    return count

def minion_game(string):
    vowels = "aiueo"
    string = string.lower()

    temp = []
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            temp.append(string[i:j])
    
    temp = list(set(temp))
    
    total = [0, 0]
    for sub in temp:
        if sub[0] in vowels:
            total[1] += count_substring(sub, string)
        else:
            total[0] += count_substring(sub, string)
    
    if total[0] == total[1]:
        print("Draw")
    else:
        print(f"Stuart {total[0]}" if total[0] > total[1] else f"Kevin {total[1]}")

if __name__ == '__main__':
    s = input()
    minion_game(s)