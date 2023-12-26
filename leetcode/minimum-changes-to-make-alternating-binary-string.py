import unittest


class Solution:
    def minOperations(self, s: str) -> int:
        zero_one_pattern = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "1":
                    zero_one_pattern += 1
            else:
                if s[i] == "0":
                    zero_one_pattern += 1
        return min(zero_one_pattern, len(s)-zero_one_pattern)


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minOperations("0100"), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.minOperations("10"), 0)

    def test_example_3(self):
        self.assertEqual(self.solution.minOperations("1111"), 2)

    def test_example_4(self):
        self.assertEqual(self.solution.minOperations("110010"), 2)

    def test_example_5(self):
        self.assertEqual(self.solution.minOperations("10010100"), 3)


if __name__ == '__main__':
    unittest.main()        

