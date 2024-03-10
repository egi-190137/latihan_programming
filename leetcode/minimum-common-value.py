class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        idx_1, idx_2 = 0, 0
        while idx_1 < len(nums1) and idx_2 < len(nums2):
            if nums1[idx_1] == nums2[idx_2]:
                return nums1[idx_1]

            if nums1[idx_1] < nums2[idx_2]:
                idx_1 += 1
            else:
                idx_2 += 1
        return -1
