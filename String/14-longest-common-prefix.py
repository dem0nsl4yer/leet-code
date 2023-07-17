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
    

# Finding the shortest term, and then looking out for the prefix. 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        key = 0 
        map = strs[0]
        for i in strs:
            if len(i) < len(map):
                map = i 
        for j in range(len(map)):
            for i in strs:
                if map[j] == i[j]:
                    continue 
                else:
                    return map[0:j] 
            key = j 
        #print(key)
        return map[0:key+1] 

