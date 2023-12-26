import unittest


class Solution:
    def numDecodings(self, s: str) -> int:
        if s == "0":
            return 0

        dp = [0 for _ in s]
        dp.append(1)

        dp[-2] = int(s[-1] != "0")

        i = len(s) - 2
        while i >= 0:
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
                if (s[i] == "1") or (s[i] == "2" and eval(s[i + 1]) < 7):
                    dp[i] += dp[i + 2]
            i -= 1
        
        return dp[0]


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.numDecodings("12"), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.numDecodings("226"), 3)

    def test_example_3(self):
        self.assertEqual(self.solution.numDecodings("06"), 0)


if __name__ == '__main__':
    unittest.main()        