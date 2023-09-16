class Solution:
    def secondHighest(self, s: str) -> int:
        k = '0123456789'
        ker1 = ker2 = -1
        for i in s:
            if i in k:
                b = int(i)
                if ker1 > b:
                    ker2 = max(b, ker2)
                elif b > ker1 :
                    ker2 = ker1
                    ker1 = b
                if ker2 ==8:
                    break 
        return ker2
