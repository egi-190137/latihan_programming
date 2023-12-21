import unittest


class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    continue
                
                is_unique = True
                for row in range(len(mat)):
                    if row == i:
                        continue
                    if mat[row][j] == mat[i][j]:
                        is_unique = False
                        break
                
                if not is_unique:
                    continue 

                for col in range(len(mat[i])):
                    if col == j:
                        continue
                    if mat[i][col] == mat[i][j]:
                        is_unique = False
                        break

                if not is_unique:
                    continue
                
                count += 1
        
        return count
    
class MyTest(unittest.main):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.numSpecial([[1,0,0],[0,0,1],[1,0,0]]), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.maxProduct([[1,0,0],[0,1,0],[0,0,1]]), 3)

if __name__ == '__main__':
    unittest.main()