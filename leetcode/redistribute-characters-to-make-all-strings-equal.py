import unittest


class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        chars = {}
        for word in words:
            for ch in word:
                chars[ch] = chars.get(ch, 0) + 1
        for count in chars.values():
            if count % len(words) > 0:
                return False
        return True
    

class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.makeEqual(words = ["abc","aabc","bc"]), True)

    def test_example_2(self):
        self.assertEqual(self.solution.makeEqual(words = ["ab","a"]), False)

    # def test_example_3(self):
    #     self.assertEqual(self.solution.getLengthOfOptimalCompression(s = "aaaaaaaaaaa", k = 0), 3)
    

if __name__ == '__main__':
    unittest.main()