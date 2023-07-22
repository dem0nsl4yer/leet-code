# Recursion based solution - exceeds time limit. 

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0 
        if n== 1:
            return 1
        if n==2:
            return 2
        return (self.climbStairs(n-2) + self.climbStairs(n-1) )


# Now memoization - with recursion. 

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def climb(n):
            memo[0] = 0 
            memo[1] = 1 
            memo[2] = 2
            if n in memo:
                return memo[n] 
            memo[n] = climb(n-2) + climb(n-1)
            return memo[n]
        return climb(n)
    
# Memoization with for loop. 

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        memo[0] = 0 
        memo[1] = 1 
        memo[2] = 2
        if n not in memo:
            for i in range(3, n+1):
                memo[i] = memo[i-1] + memo[i-2]
        return memo[n]

# Listing 
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        listt = [0]* (n+1)
        listt[1] = 1 
        listt[2] = 2
        for i in range (3, n+1):
            listt[i] = listt[i-1] + listt[i-2]
        return listt[n]


# Iterative solution
class Solution:
    def climbStairs(self, n: int) -> int:
        one,two=1,1
        for i in range(n-1):
            temp=one+two
            one=two
            two=temp
        return two
    

# Cleaned up listing 
class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]