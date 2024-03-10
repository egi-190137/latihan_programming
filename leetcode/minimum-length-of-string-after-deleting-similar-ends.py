class Solution:
    def minimumLength(self, s: str) -> int:
        idx_start = 0
        idx_end = len(s) - 1
        while True:
            if s[idx_start] != s[-1]:
                break

            while s[idx_start] == s[idx_start + 1]:
                idx_start += 1

            while s[idx_end] == s[idx_end - 1]:
                idx_end -= 1

        return idx_end - idx_start + 1
