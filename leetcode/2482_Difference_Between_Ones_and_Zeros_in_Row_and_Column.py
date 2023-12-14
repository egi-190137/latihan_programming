import unittest


class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        diff = [ [ 0 for j in range(len(grid[i])) ] for i in range(len(grid)) ]

        zero_col = [ 0 for i in range(len(grid[0])) ]
        one_col = [ 0 for i in range(len(grid[0])) ] 
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if grid[j][i] == 0:
                    zero_col[i] += 1
                else:
                    one_col[i] += 1

        for i in range(len(grid)):
            zero_row = 0
            one_row = 0
            for num in grid[i]:
                if num == 0:
                    zero_row += 1
                else:
                    one_row += 1

            for j in range(len(grid[i])):
                diff[i][j] = one_row + one_col[j] - zero_row - zero_col[j]
        
        return diff
    

class MyTest(unittest.main):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]], [[0,0,4],[0,0,4],[-2,-2,2]]))

    def test_example_2(self):
        self.assertEqual(self.solution.maxProduct([[1,1,1],[1,1,1]], [[5,5,5],[5,5,5]]))

if __name__ == '__main__':
    unittest.main()