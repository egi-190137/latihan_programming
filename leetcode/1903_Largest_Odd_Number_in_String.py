import unittest


class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 > 0:
                return num[:i+1]
        return ""
        # num = int(num)
        # while num > 0:
        #     if num % 2 > 0:
        #         return str(num)
        #     num //= 10
        # return ""
            
class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.largestOddNumber("52"), "5")

    def test_example_2(self):
        self.assertEqual(self.solution.largestOddNumber("4206"), "")

    def test_example_3(self):
        self.assertEqual(self.solution.largestOddNumber("35427"), "35427")

if __name__ == '__main__':
    unittest.main()