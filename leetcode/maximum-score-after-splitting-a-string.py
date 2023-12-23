import unittest


class Solution:
    def maxScore(self, s: str) -> int:
        left_value = 0 if s[0] == "1" else 1
        right_value = 0
        for i in range(1, len(s)):
            if s[i] == "1":
                right_value += 1
        
        max_score = left_value + right_value
        
        for i in range(1, len(s)-1):
            if s[i] == "0":
                left_value += 1
            else:
                right_value -= 1
        
            if left_value + right_value > max_score:
                max_score = left_value + right_value

        return max_score


class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxScore("011101"), 5)

    def test_example_2(self):
        self.assertEqual(self.solution.maxScore("00111"), 5)

    def test_example_3(self):
        self.assertEqual(self.solution.maxScore("1111"), 3)


if __name__ == '__main__':
    unittest.main()        