class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [0] *(n)
        memo[0] = cost[0]
        memo[1] = cost[1]
        for i in range(2, n):
            memo[i] = cost[i] + min(memo[i-1], memo[i-2])
        # memo already has cost of being at a floor added on it. 
        return min(memo[-1], memo[-2])