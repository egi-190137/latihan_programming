def h_index(n, citations):
    ans = []
    # TODO: Complete the function to get the H-Index scores after each paper
    for i in range(n):
        temp = 1
        while True:
            count = 0
            for j in range(0, i+1):
                if (citations[j] >= temp):
                    count += 1
            
            if count < temp:
                break

            temp += 1
        
        ans.append(temp-1)              

    return ans


if __name__ == '__main__':
    t = int(input())

    for test_case in range(1, t + 1):
        n = int(input())                     # The number of papers
        citations = list(map(int, input().split())) # The number of citations for each paper
        h_index_scores = h_index(n, citations)
        print("Case #" + str(test_case) + ": " + ' '.join(map(str, h_index_scores)))