class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maps = {}
        for num in nums:
            maps[num] = maps.get(num, 0) + 1

        nums_list = list(maps.keys())
        majority = nums_list[0]
        for i in range(1, len(nums_list)):
            if maps[nums_list[i]] > maps[majority]:
                majority = nums_list[i]
        return majority
