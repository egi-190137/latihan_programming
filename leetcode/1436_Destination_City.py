import unittest


class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        if len(paths) == 1:
            return paths[0][1]
        
        idx_begin_sorted = len(paths) - 1
        idx_check_path = idx_begin_sorted - 1
        while idx_check_path >= 0:
            if paths[-1][1] == paths[idx_check_path][0]:
                paths.append(paths.pop(idx_check_path))
                idx_begin_sorted -= 1
                idx_check_path = idx_begin_sorted - 1
                continue

            idx_check_path -= 1

        return paths[-1][1]

        
class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(
            self.solution.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]), "Sao Paulo"
        )

    def test_example_2(self):
        self.assertEqual(
            self.solution.destCity([["B","C"],["D","B"],["C","A"]]), "A"
        )

    def test_example_3(self):
        self.assertEqual(
            self.solution.destCity([["A","Z"]]), "Z"
        )
    
    def test_example_4(self):
        self.assertEqual(
            self.solution.destCity([["jMgaf WaWA","iinynVdmBz"],[" QCrEFBcAw","wRPRHznLWS"],["iinynVdmBz","OoLjlLFzjz"],["OoLjlLFzjz"," QCrEFBcAw"],["IhxjNbDeXk","jMgaf WaWA"],["jmuAYy vgz","IhxjNbDeXk"]]), "wRPRHznLWS"
        )


if __name__ == '__main__':
    unittest.main()