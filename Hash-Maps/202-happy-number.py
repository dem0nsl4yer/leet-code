class Solution:
    def isHappy(self, n: int) -> bool:
        set = []
        def squares(n):
            k = str(n)
            ctr = 0 
            for i in k:
                ctr += int(i)*int(i)
            return ctr 
        count = 0 
        while(n != 1):
            n = squares(n)
            if n in set:
                return False
            set.append(n)
        return True 