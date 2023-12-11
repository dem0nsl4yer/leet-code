# Basic solution 

class Solution:
    def reverseWords(self, s: str) -> str:
        # Read all words
        # Reverse order - output

        word = False 
        count = []
        words = ''
        for i in s:
            if i == ' ':
                if word:
                    count.append(words)
                    words = ''
                    word = False 
            else:
                words += i
                word = True 
        if word:
            count.append(words)
        reversed_string = ' '.join(reversed(count))
        return reversed_string
    
# Solution 2: 
# Split, join-reverse. 
class Solution:
    def reverseWords(self, s: str) -> str:
        # Read all words
        # Reverse order - output
        b = s.split()
        reversed_string = ' '.join(reversed(b))
        return reversed_string