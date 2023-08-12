class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = ['A']
        for i in s:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack[1:])
    

# Slight cleanup 

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)