import unittest



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return

class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]), 3)


if __name__ == '__main__':
    unittest.main()