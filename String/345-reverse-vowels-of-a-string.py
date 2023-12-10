class Solution:
    def reverseVowels(self, s: str) -> str:
        # Pull all vowels, push all of them in a stack. 
        # Pop them - first in, last out. 
        vowel = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        result = ''
        stack = []
        for i in s:
            if i in vowel:
                stack.append(i)
        for i in s:
            if i in vowel:
                result += stack.pop()
            else:
                result += i 
        return(result)

# 2ptr approach

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s)-1 # Init the left and rht ptrs. 
        vowels = set('AEIOUaeiou') # vowel str. 
        while left<right:
            while left<right and s[left] not in vowels: # continuity - left<right, -> reach a vowel 
               left += 1 
            while left<right and s[right] not in vowels: # --> reach a vowel. 
               right -= 1 
            s[left],s[right] = s[right],s[left] # When both left and right reach vowel, swap them
            left += 1 # continue loop at the next ptrs. 
            right -= 1
        s = "".join(s)
        return s