# Does not works - wrong interpretation of question. 

class Solution:
    def makeGood(self, s: str) -> str:
        k = []
        add = True 
        for i in range(len(s)):
            if s[i].isupper():
                if len(k) != 0:
                    k.pop()
                else:
                    add = False 
            elif add == True:
                k.append(s[i])
        return ''.join(k)


#working solution needs the internal filter revised to remove the paired functions. 

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)