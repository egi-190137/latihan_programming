import unittest

class Solution:

    def countCharacters(self, words: list[str], chars: str) -> int:
        dict_chars = {}
        for char in chars:
            dict_chars[char] = dict_chars.get(char, 0) + 1

        result = 0
        for word in words:
            is_formed = True
            dict_word = {}
            for char in word:
                if char not in dict_chars.keys():
                    is_formed = False
                    break

                dict_word[char] = dict_word.get(char, 0) + 1
                if dict_word[char] > dict_chars[char]:
                    is_formed = False
                    break

            if is_formed:
                result += len(word)

        return result
        
class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(
            self.solution.countCharacters(
                words = ["cat","bt","hat","tree"], 
                chars = "atach"),
            6
        )

    def test_example_2(self):
        self.assertEqual(
            self.solution.countCharacters(
                words = ["hello","world","leetcode"],
                chars = "welldonehoneyr"),
            10
        )


if __name__ == '__main__':
    unittest.main()