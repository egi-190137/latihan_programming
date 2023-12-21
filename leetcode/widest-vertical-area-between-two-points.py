import unittest


class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[0])

        max_width = 0

        for i in range(1, len(points)):
            width = points[i][0] - points[i-1][0]
            max_width = max(max_width, width)

        return max_width


class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]), 3)


if __name__ == '__main__':
    unittest.main()