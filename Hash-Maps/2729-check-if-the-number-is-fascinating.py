class Solution:
    def isFascinating(self, n: int) -> bool:
        a = str(n) + str(2*n) + str(3*n)
        test = '123456789'
        if '0' in a:
            return False 
        if len(a) >9:
            return False 
        for i in test:
            if i in a:
                continue 
            else:
                return False 
        return True 
        