class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        first_negative_idx = None
        first_positive_idx = None
        for i in range(len(nums) - 1):
            if i % 2 == 0 and nums[i] > 0 or i % 2 != 0 and nums[i] < 0:
                continue
            if i % 2 == 0:
                if first_positive_idx:
                    if first_positive_idx > i:
                        start = first_positive_idx
                    else:
                        start = i + 1
                else:
                    start = i + 1
            else:
                if first_negative_idx:
                    if first_negative_idx > i:
                        start = first_negative_idx
                    else:
                        start = i + 1
                else:
                    start = i + 1
            for j in range(start, len(nums)):
                if i % 2 == 0 and nums[j] > 0 or i % 2 != 0 and nums[j] < 0:
                    nums.insert(i, nums.pop(j))
                    if i % 2 == 0:
                        first_positive_idx = j + 1
                    else:
                        first_negative_idx = j + 1
                    break
        return nums


solution = Solution()
# print(solution.rearrangeArray(nums=[3, 1, -2, -5, 2, -4]))
print(
    solution.rearrangeArray(
        nums=[
            28,
            -41,
            22,
            -8,
            -37,
            46,
            35,
            -9,
            18,
            -6,
            19,
            -26,
            -37,
            -10,
            -9,
            15,
            14,
            31,
        ]
    )
)
