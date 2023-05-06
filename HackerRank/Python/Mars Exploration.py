def marsExploration(s):
    sos_message = "SOS"
    count = 0
    for i in range(len(s)):
        if s[i] != sos_message[i%3]:
            count += 1
            
    return count

if __name__ == '__main__':

    s = input()

    result = marsExploration(s)

    print(result)