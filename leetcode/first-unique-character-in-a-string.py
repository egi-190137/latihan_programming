class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}
        for ch in s:
            chars[ch] = chars.get(ch, 0) + 1

        for i in range(len(s)):
            if chars[s[i]] == 1:
                return i
        return -1

