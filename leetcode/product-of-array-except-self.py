class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dot_prod = 1
        count_zero = 0
        for num in nums:
            if num == 0:
                count_zero += 1
            else:
                dot_prod *= num

            if count_zero > 1:
                return [0] * len(nums)
        if count_zero == 1:
            return [0 if num else dot_prod for num in nums]
        return [int(dot_prod / num) for num in nums]
