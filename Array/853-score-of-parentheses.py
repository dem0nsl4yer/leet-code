class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        bal = []
        if s == '':
            return 0 
        elif s == '()':
            return 1 
        sum = 0 
        for i in range(len(s)):
            if s[i] == '(':
                bal.append('(')
            if s[i] == ')' and len(bal) > 0 :
                bal.pop()
                if s[i-1] == '(':
                    sum += 2 **(len(bal)-1)
        return sum 


# working code 

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        
        for char in s:
            if char == '(':
                stack.append(score)
                score = 0
            else:
                prev_score = stack.pop()
                score = prev_score + max(2 * score, 1)
        
        return score

# Also works 

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        
        for char in s:
            if char == '(':
                stack.append('a')
                multiply = True 
            else:
                if multiply == True:
                    score +=  2**(len(stack)-1)
                    multiply = False 
                stack.pop()
        return score
