import unittest

class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        result = [ [ 0 for j in range(len(img[i])) ] for i in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[i])):
                cell_count = 0
                cell_sum = 0
                for k in range(i-1, i+2):
                    if k < 0 or k >= len(img):
                        continue

                    for l in range(j-1, j+2): 
                        if l < 0 or l >= len(img[k]):
                            continue

                        cell_count += 1
                        cell_sum += img[k][l]

                result[i][j] = cell_sum // cell_count

        return result 
                
class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(
            self.solution.imageSmoother(
                [[1,1,1],[1,0,1],[1,1,1]]
            ), 
            [[0,0,0],[0,0,0],[0,0,0]]
        )

    def test_example_2(self):
        self.assertEqual(
            self.solution.imageSmoother(
                [[100,200,100],[200,50,200],[100,200,100]]
            ), 
            [[137,141,137],[141,138,141],[137,141,137]]
        )


if __name__ == '__main__':
    unittest.main()