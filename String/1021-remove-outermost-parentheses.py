class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        z = ''
        k = []
        if s is None:
            return None 
        store = False 
        for i in s:
            if i == '(':
                store = True 
                k.append(0)
            if len(k) < 2:
                store = False 
            if store == True:
                z += i
            if i == ')':
                k.pop()
        return z 
