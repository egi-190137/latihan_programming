class Solution:
    def frequencySort(self, s: str) -> str:
        char_counts = {}
        for ch in s:
            char_counts[ch] = char_counts.get(ch, 0) + 1

        chars = list(char_counts.keys())
        res = ""
        for i in range(len(chars)):
            for j in range(i + 1, len(chars)):
                if char_counts[chars[i]] < char_counts[chars[j]]:
                    chars[i], chars[j] = chars[j], chars[i]

            res += chars[i] * char_counts[chars[i]]
        return res
