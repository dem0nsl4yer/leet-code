class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = Counter(s)

        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
        
        return -1
    
## Building blocks. 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        for i in s:
            if i in char_count:
                char_count[i] += 1
            else:
                char_count[i] = 1

        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
        
        return -1