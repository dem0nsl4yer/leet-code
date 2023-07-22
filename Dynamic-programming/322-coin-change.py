# Partial - unresolved. 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        counter = 0 
        while (amount != 0 and coins):
            k = max(coins)
            if amount >= k:
                m = amount%k 
                counter += amount//k 
                amount = m 
            coins.remove(k)
        if amount != 0:
            return -1 
        return counter 
