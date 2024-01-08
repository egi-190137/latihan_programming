import bisect
import unittest


class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dfs(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]
            
            res = dfs(i + 1)

            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = res = max(res, intervals[i][2] + dfs(j))
            return res
        
        return dfs(0)
    
class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]), 120)

    def test_example_2(self):
        self.assertEqual(self.solution.jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]), 150)

    def test_example_3(self):
        self.assertEqual(self.solution.jobScheduling(startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]), 6)


if __name__ == '__main__':
    unittest.main()
        