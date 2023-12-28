import unittest


class Solution:
    def compress(self, chars: list[str]) -> int:
        # current_consecutive = [chars[0], 1]
        # result = ""
        # for i in range(1, len(chars)):
        #     if chars[i] != current_consecutive[0]:
        #         result += current_consecutive[0] + str(current_consecutive[1])
        #         current_consecutive = [chars[i], 1]
        #     else:
        #         current_consecutive[1] += 1
        # result += current_consecutive[0] + str(current_consecutive[1])
        # return len(result)



        first_occurance = 0
        idx = 1
        num_chars = 1
        while idx < len(chars):
            if chars[idx] == chars[first_occurance]:
                num_chars += 1
                idx += 1
            else:
                if num_chars > 1:
                    freq = str(num_chars)
                    chars = chars[:first_occurance+1] + [ digit for digit in freq ] + chars[idx:]
                    first_occurance += len(freq) + 1
                else:
                    chars = chars[:first_occurance+1] + chars[idx:]
                    first_occurance += 1
                idx = first_occurance + 1
                num_chars = 1
        if num_chars > 1:
            freq = str(num_chars)
            chars = chars[:first_occurance+1] + [ digit for digit in freq ] + chars[idx:]
        else:
            chars = chars[:first_occurance+1] + chars[idx:]
        return len(chars)

        # curr = chars[0]
        # amount = 1
        # result = []
        # for i in range(1, len(chars)):
        #     if chars[i] == curr:
        #         amount += 1
        #     else:
        #         result += [ curr ]
        #         if amount > 1:
        #             result += [digit for digit in str(amount)]
        #         curr = chars[i]
        #         amount = 1
        # result += [ curr ]
        # if amount > 1:
        #     result += [digit for digit in str(amount)]
        # chars = result
        # print(chars)
        # return len(chars)


class MyTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.compress(chars = ["a","a","b","b","c","c","c"]), 6)

    def test_example_2(self):
        self.assertEqual(self.solution.compress(chars = ["a"]), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]), 4)


if __name__ == '__main__':
    unittest.main()