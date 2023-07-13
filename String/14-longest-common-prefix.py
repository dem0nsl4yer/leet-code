class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        d = ''
        for j in range(len(strs[0])):
            try:
                for i in range(len(strs)):
                    if strs[0][j] != strs[i][j]:
                        return d
                d += strs[0][j] 
            except IndexError:
                return d
        return d