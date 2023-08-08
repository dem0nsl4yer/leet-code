class Solution:
    def mySqrt(self, x: int) -> int:
        k = {
            0: 0,
            1 : 1,
            5: 25, 
            10: 100,
            50: 2500,
            100:10000,
            500: 250000,
            1000: 1000000
        }
        for i in k:
            if x <= k[i]:
                key = i 
                break 
            for l in range(key):
                if l**2 > x:
                    return l-1