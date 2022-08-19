def pickingNumbers(a):
    nums = {}
    if len(set(a)) > 1:
        for num in a:
            if num not in nums.keys():
                nums[num] = 1
            else:
                nums[num] += 1
        
        keys = sorted(nums.keys())
        subLength = []
        for i in range(len(keys) - 1):
            if keys[i+1] - keys[i] == 1:
                subLength.append(nums[keys[i]] + nums[keys[i+1]])
            else:
                subLength.append(nums[keys[i]])
        
        return max(subLength)
    else:
        return len(a)


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(result)