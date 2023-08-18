class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        k = s.split(' ')
        hash = {}
        hashb = {}
        if len(k) != len(pattern):
            return False 
        for i in range(len(pattern)):
            if pattern[i] not in hash and k[i] not in hashb:
                hash[pattern[i]] = k[i]
                hashb[k[i]] = pattern[i]
            elif pattern[i] in hash and hash[pattern[i]] != k[i]:
                return False 
            elif k[i] in hashb and hashb[k[i]] != pattern[i]:
                return False
        
        return True