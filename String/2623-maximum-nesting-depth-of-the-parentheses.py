class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        counter = 0 
        for i in s:
            if i == '(':
                stack.append('(')
                counter = max(counter, len(stack))
            elif i == ')':
                stack.pop()
        return counter 
