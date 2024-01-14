class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != word2:
            return False

        dict_1 = {}
        dict_2 = {}
        for ch in word1:
            dict_1[ch] = dict_1.get(ch, 0) + 1

        for ch in word2:
            dict_2[ch] = dict_2.get(ch, 0) + 1
        
        return dict_1.keys() == dict_2.keys() and dict_1.values() == dict_2.values()
