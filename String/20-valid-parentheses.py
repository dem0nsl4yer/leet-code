class Solution:
    def isValid(self, s: str) -> bool:
        k = {'{':'}', '(':')', '[':']'}
        z = 1
        res = []
        for i in range(len(s)):
            if s[i] in k:
                res.append(s[i])
                #print(res[-1])
            elif s[i] not in k and len(res)>0:
                if k[res[-1]] == s[i]:
                    res.pop()
                else:
                    return False
            else:
                return False 
        if len(res) >0:
            return False 
        return True 
    


    ########### Shorter version 


    class Solution:
    def isValid(self, s: str) -> bool:
        opening_brackets = {'{', '(', '['}
        matching_brackets = {'}': '{', ')': '(', ']': '['}
        stack = []
        
        for char in s:
            if char in opening_brackets:
                stack.append(char)
            elif char in matching_brackets:
                if not stack or stack.pop() != matching_brackets[char]:
                    return False
                    
        return len(stack) == 0