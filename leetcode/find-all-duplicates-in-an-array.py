class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        setNum = set()
        res = []
        for num in nums:
            if num not in setNum:
                setNum.add(num)
            else:
                res.append(num)
        return res
