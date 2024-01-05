import unittest


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n
        print(dp)

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    print(dp)

        return max(dp)


class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.lengthOfLIS(nums = [10,9,2,5,3,7,101,18]), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.lengthOfLIS(nums = [0,1,0,3,2,3]), 4)

    def test_example_3(self):
        self.assertEqual(self.solution.lengthOfLIS(nums = [7,7,7,7,7,7,7]), 1)


if __name__ == '__main__':
    unittest.main()