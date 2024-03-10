class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_one = 0
        for ch in s:
            if ch == "1":
                count_one += 1

        res = ""
        res += "1" * (count_one - 1)
        res += "0" * (len(s) - count_one) + "1"
        return res
