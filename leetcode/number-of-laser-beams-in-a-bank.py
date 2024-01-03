import unittest


class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        total = 0
        prev_row = 0
        curr_row = 0
        for i in range(len(bank)):
            for j in range(len(bank[i])):
                if bank[i][j] == "1":
                    curr_row += 1
            
            if curr_row == 0:
                continue
            total += prev_row * curr_row
            prev_row = curr_row
            curr_row = 0
        return total

    

class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.numberOfBeams(bank = ["011001","000000","010100","001000"]), 8)

    def test_example_2(self):
        self.assertEqual(self.solution.numberOfBeams(bank = ["000","111","000"]), 0)


if __name__ == '__main__':
    unittest.main()