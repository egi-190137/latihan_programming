import unittest


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[9999] * 110 for _ in range(110)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(0, k + 1):
                cnt, del_ = 0, 0
                for l in range(i, 0, -1):
                    if s[l - 1] == s[i - 1]:
                        cnt += 1
                    else:
                        del_ += 1

                    if j - del_ >= 0:
                        dp[i][j] = min(dp[i][j], dp[l - 1][j - del_] + 1 + (3 if cnt >= 100 else 2 if cnt >= 10 else 1 if cnt >= 2 else 0))

                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])

        return dp[n][k]


        

class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.getLengthOfOptimalCompression(s = "aaabcccd", k = 2), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.getLengthOfOptimalCompression(s = "aabbaa", k = 2), 2)

    def test_example_3(self):
        self.assertEqual(self.solution.getLengthOfOptimalCompression(s = "aaaaaaaaaaa", k = 0), 3)
    

if __name__ == '__main__':
    unittest.main()