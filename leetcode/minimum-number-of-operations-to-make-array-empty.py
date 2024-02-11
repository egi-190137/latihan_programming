import unittest


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        amount_nums = {}
        for num in nums:
            amount_nums[num] = amount_nums.get(num, 0) + 1
        print(amount_nums)
        operation = 0
        for amount in amount_nums.values():
            if amount > 4:
                if (amount - 4) % 3 == 0:
                    operation += (amount - 4) // 3 + 2
                    continue
            if amount > 2:
                if (amount - 2) % 3 == 0:
                    operation += (amount - 2) // 3 + 1
                    continue
            if amount % 3 == 0:
                operation += amount // 3
                continue
            if amount % 2 == 0:
                operation += amount // 2
                continue
            operation = -1
            break
        return operation


class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(
            self.solution.minOperations(nums=[2, 3, 3, 2, 2, 4, 2, 3, 4]), 4
        )

    def test_example_2(self):
        self.assertEqual(self.solution.minOperations(nums=[2, 1, 2, 2, 3, 3]), -1)

    def test_example_3(self):
        self.assertEqual(
            self.solution.minOperations(
                nums=[
                    14,
                    12,
                    14,
                    14,
                    12,
                    14,
                    14,
                    12,
                    12,
                    12,
                    12,
                    14,
                    14,
                    12,
                    14,
                    14,
                    14,
                    12,
                    12,
                ]
            ),
            7,
        )


if __name__ == "__main__":
    unittest.main()
