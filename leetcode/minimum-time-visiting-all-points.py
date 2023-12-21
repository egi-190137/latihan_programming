import unittest

class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        total_distance = 0
        for i in range(len(points) - 1):
            distance = [ 
                points[i+1][0] - points[i][0], 
                points[i+1][1] - points[i][1],
            ]
            distance[0] = distance[0] if distance[0] >= 0 else distance[0] * -1
            distance[1] = distance[1] if distance[1] >= 0 else distance[1] * -1
            total_distance += max(distance)

        return total_distance

        
class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(
            self.solution.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]), 7
        )

    def test_example_2(self):
        self.assertEqual(
            self.solution.minTimeToVisitAllPoints([[3,2],[-2,2]]), 5
        )


if __name__ == '__main__':
    unittest.main()