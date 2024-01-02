import unittest


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        matrix = [set()]
        for num in nums:
            is_exist = True
            for i in range(len(matrix)):
                if num not in matrix[i]:
                    matrix[i].add(num)
                    is_exist = False
                    break
            if is_exist:
                matrix.append(set([num]))
        return [ list(row) for row in matrix ]
    

class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.findMatrix(nums = [1,3,4,1,2,3,1]), [[1,3,4,2],[1,3],[1]])

    def test_example_2(self):
        self.assertEqual(self.solution.findMatrix(nums = [1,2,3,4]), [[4,3,2,1]])


if __name__ == '__main__':
    unittest.main()