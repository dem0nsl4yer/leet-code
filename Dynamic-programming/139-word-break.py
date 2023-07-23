class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        while(len(s)>0):
            found = False 
            for i in wordDict:
                if i[0:len(i)] == s[0:len(i)]:
                    s = s[len(i):]
                    found = True 
                    break   
            if not found:
                return False     
        return True  
