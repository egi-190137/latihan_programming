import unittest


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        for i in range(2):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return (nums[0] - 1) * (nums[1] - 1)

class MyTest(unittest.main):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxProduct([3,4,5,2]), 12)

    def test_example_2(self):
        self.assertEqual(self.solution.maxProduct([1,5,4,5]), 16)

    def test_example_3(self):
        self.assertEqual(self.solution.maxProduct([3, 7]), 12)

if __name__ == '__main__':
    unittest.main()