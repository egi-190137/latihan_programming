import unittest


class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        total_time = 0
        i = 1
        previous_i = 0
        while i < len(colors) :
            if colors[previous_i] != colors[i]:
                previous_i = i
                i += 1
                continue

            if neededTime[previous_i] < neededTime[i]:
                total_time += neededTime[previous_i]
                previous_i = i
                i += 1
            else:
                total_time += neededTime[i]
                i += 1
        return total_time

    
class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minCost(colors = "abaac", neededTime = [1,2,3,4,5]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.minCost(colors = "abc", neededTime = [1,2,3]), 0)

    def test_example_3(self):
        self.assertEqual(self.solution.minCost(colors = "aabaa", neededTime = [1,2,3,4,1]), 2)

    def test_example_4(self):
        self.assertEqual(self.solution.minCost(colors = "aaabbbabbbb", neededTime = [3,5,10,7,5,3,5,5,4,8,1]), 26)


if __name__ == '__main__':
    unittest.main()