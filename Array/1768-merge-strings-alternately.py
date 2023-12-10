# Basic solution - 2 pass
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = ''
        while(word1 and word2):
            out += word1[0]
            word1 = word1[1:]
            out += word2[0]
            word2 = word2[1:]
        if word1:
            out += word1
        else:
            out += word2
        return out
    
# Single pass - indexing. 

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = ''
        i, j = 0,0
        len1, len2 = len(word1), len(word2)

        while(i<len1 and j <len2):
            out += word1[i] + word2[j]
            i += 1
            j += 1
        out += word1[i:] + word2[j:]
        return out