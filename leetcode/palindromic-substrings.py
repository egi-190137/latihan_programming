import unittest


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s):
                print(s[l : r + 1])
                if s[l] != s[r]:
                    break

                # if s[l : r + 1] in temp:
                #     l -= 1
                #     r += 1
                #     continue

                res += 1
                l -= 1
                r += 1

        for i in range(len(s) - 1):
            l, r = i, i + 1
            while l >= 0 and r < len(s):
                print(s[l : r + 1])
                if s[l] != s[r]:
                    break

                # if s[l : r + 1] in temp:
                #     l -= 1
                #     r += 1
                #     continue

                res += 1
                l -= 1
                r += 1

        return res


class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.countSubstrings(s="abc"), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.countSubstrings(s="aaa"), 6)


if __name__ == "__main__":
    unittest.main()
