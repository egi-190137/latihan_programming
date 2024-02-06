class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            result["".join(sorted(string))] = result.get("".join(sorted(string)), []) + [ string ]

        return [ group for group in result.values() ]
