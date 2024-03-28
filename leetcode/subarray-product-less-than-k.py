class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        prev_prod = prev_count = None
        for i in range(len(nums)):
            tmp = nums[i]
            if i == 0:
            for j in range(i, len(nums)):
                if j > i:
                    tmp *= nums[j]

                if tmp >= k:
                    break
                count += 1
        return count
