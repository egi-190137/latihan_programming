class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1, 3-1, -1):
            other_side = sum(nums[:i])
            if nums[i] < other_side:
                return nums[i] + other_side
        return -1
