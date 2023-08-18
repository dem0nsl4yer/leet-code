class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        out = ''
        if len(num1) >= len(num2):
            j = num1
            k = num2
        else:
            k = num1
            j = num2
        rem = 0 
        p1, p2 = len(j) - 1, len(k) - 1  # Pointers to track current positions
        
        while p1 >= 0 or p2 >= 0:  # Iterate from right to left
            if p1 >= 0:
                rem += int(j[p1])
                p1 -= 1
            if p2 >= 0:
                rem += int(k[p2])
                p2 -= 1
            out = str(rem % 10) + out  # Append digit to the left of the output
            rem = rem // 10  # Update carry
        
        if rem:
            out = str(rem) + out
        
        return out





