class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = strs[0]
        res = ""
        for i in strs:
            if len(i) < len(shortest):
                shortest = i
        
        for i in range(len(strs)):
            for j in range(len(shortest)):
                if shortest[j] != strs[i][j]:
                    shortest = shortest[:j]
                    break
        return shortest

        
        