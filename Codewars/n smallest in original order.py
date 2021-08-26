def first_n_smallest(arr, n):
    ori = arr
    for i in range(len(arr)):
        # print("i = " + str(i))
        for j in range(len(arr) - 1, i, -1):
            # print("j = " + str(j))
            if arr[j] < arr[j - 1]:
                [ arr[j], arr[j - 1] ] = [ arr[j - 1], arr[j] ]
    
    temp = arr[0:n]
    for i in range(len(temp)):
        # print("i = " + str(i))
        for j in range(len(temp) - 1, i, -1):
            # print("j = " + str(j))
            if ori.index(temp[j]) > ori.index(temp[j - 1]):
                [ temp[j], temp[j - 1] ] = [ temp[j - 1], temp[j] ]

    return temp

print(first_n_smallest([5,4,3,2,1],3), [3,2,1])
print(first_n_smallest([1,2,3,4,1],3), [1,2,1])
print(first_n_smallest([1,2,3,4,5],3), [1,2,3])
print(first_n_smallest([1,2,3,-4,0],3), [1,-4,0])
print(first_n_smallest([1,2,3,4,5],0), [])