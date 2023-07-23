class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        memo = [0] *n
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])
        for i in range(2, n):
            memo[i] = max(nums[i] + memo[i - 2], memo[i - 1])
        return memo[-1]
    
    # Just figure out which block to choose by iterative comparison. 