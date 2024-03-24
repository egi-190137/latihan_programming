class Solution:
    def customSortString(self, order: str, s: str) -> str:
        idx_chars = {}
        chars = [ch for ch in s]
        for ch in chars:
            try:
                idx_chars[ch] = order.index(ch)
            except ValueError:
                idx_chars[ch] = -1
        return "".join(sorted(chars, key=lambda ch: idx_chars[ch]))
