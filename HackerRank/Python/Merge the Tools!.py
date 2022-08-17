def merge_the_tools(string, k):
    arr = []
    # print(temp)
    for i in range(0, len(string), k):
        arr.append(string[i:i+k])
        # print(i)
    # print(temp)
    for i in range(len(arr)):
        temp = ""
        for ch in arr[i]:
            if ch not in temp:
                temp += ch
        
        print(temp)

if __name__ == '__main__':
    temp = input().split()
    string, k = temp[0], int(temp[1])
    merge_the_tools(string, k)