"""Starter Code for Milk Tea CC Problem"""

# Complete the count_complaints function
def matchStringArr(string, arrString):
    for word in arrString:
        if word == string:
            return True
    return False


def count_complaints(preferences, forbiddens):
    complaints = []
    # TODO: Add logic to count the number of complaints
    temp = []
    for i in range(len(preferences[0])):
        # Hitung angka 1
        count = 0
        for j in range(len(preferences)):
            if preferences[j][i] == '1':
                count += 1
        if len(preferences) - count > count: # angka 0 lebih banyak dari angka 1
            temp.append('0')
            complaints.append(count)
        else:
            temp.append('1')
            complaints.append(len(preferences) - count)
    
    # print(temp)
    # print(complaints)
    # print(''.join(temp))
    
    while matchStringArr(''.join(temp), forbiddens):
        idxTerbesar = 0
        for i in range(1, len(complaints)):
            if complaints[idxTerbesar] < complaints[i]:
                idxTerbesar = i
        
        complaints[idxTerbesar] = len(preferences) - complaints[idxTerbesar]
        temp[idxTerbesar] = '1' if temp[idxTerbesar] == '0' else '0'
    
    # print(temp)
    # print(complaints)

    return sum(complaints)





#   return complaints

if __name__ == '__main__':
    # Read number of test cases
    num_cases = int(input())

    for tc in range(1, num_cases + 1):
        # Read number of friends, number of forbidden teas, and number of options
        num_friends, num_forbidden, num_options = map(int, input().split())

        # Read the friends' preferences
        preferences = [input() for _ in range(num_friends)]

        # Read the forbidden teas
        forbiddens = [input() for _ in range(num_forbidden)]

        print("Case #%d: %d" % (tc, count_complaints(preferences, forbiddens)))