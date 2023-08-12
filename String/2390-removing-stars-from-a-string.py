class Solution:
    def removeStars(self, s: str) -> str:
        k = ''
        for i in s:
            if i != '*':
                k += i 
            if i == '*':
                k = k[:-1]
        return k 


# Another solution 

class Solution:
    def removeStars(self, s: str) -> str:
        k = []
        for i in s:
            if i != '*':
                k.append(i)
            if i == '*':
                k.pop()
        return "".join(k)