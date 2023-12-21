import unittest


class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1

          
class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.numberOfMatches(7), 6)

    def test_example_2(self):
        self.assertEqual(self.solution.numberOfMatches(14), 13)


if __name__ == '__main__':
    unittest.main()