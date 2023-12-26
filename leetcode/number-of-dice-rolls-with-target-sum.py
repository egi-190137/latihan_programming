import unittest


class Solution:
    mod = 10 ** 9 + 7

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[-1] * (target + 1) for _ in range(n + 1)]
        return self.recursion(dp, n, k, target)

    def recursion(self, dp: list, n: int, k: int, target: int) -> int:
        if target == 0 and n == 0:
            return 1
        if n == 0 or target <= 0:
            return 0

        if dp[n][target] != -1:
            return dp[n][target] % self.mod

        ways = 0
        for i in range(1, k + 1):
            ways = (ways + self.recursion(dp, n - 1, k, target - i)) % self.mod

        dp[n][target] = ways % self.mod
        return dp[n][target]


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.numRollsToTarget(n = 1, k = 6, target = 3), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.numRollsToTarget(n = 2, k = 6, target = 7), 6)

    def test_example_3(self):
        self.assertEqual(self.solution.numRollsToTarget(n = 30, k = 30, target = 500), 222616187)


if __name__ == '__main__':
    unittest.main()        

