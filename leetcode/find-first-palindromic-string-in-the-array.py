class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            for i in range(len(word) // 2):
                isPalindrome = True
                if word[i] != word[-1 - i]:
                    isPalindrome = False
                    break

            if isPalindrome:
                return word
        return ""
