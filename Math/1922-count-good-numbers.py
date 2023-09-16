class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
#        prime = ['2', '3', '5', '7']
#        even = ['0', '2', '4', '6', '8']
        num = 1
        for i in range(n):
            if i %2 == 0:
                num = num*5
            else:
                num = num*4
        return num%MOD
    
#faster - working solution 

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
#        prime = ['2', '3', '5', '7']
#        even = ['0', '2', '4', '6', '8']
        # Calculate the number of good numbers of even length (even positions)
        even_count = pow(5, (n+1) // 2, MOD)

        # Calculate the number of good numbers of odd length (odd positions)
        # If n is odd, multiply by 4 for the last position
        odd_count = pow(4, n // 2, MOD)

        # Multiply the counts to get the total count
        total_count = (even_count * odd_count) % MOD

        return total_count