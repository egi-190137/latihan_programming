from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = sorted(list(Counter(nums).values()), reverse=True)

        res = counts[0]
        for i in range(1, len(counts)):
            if counts[i] != counts[0]:
                break
            res += counts[i]
        return res
