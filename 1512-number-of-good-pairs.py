class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        k = len(nums)
        for i in range(k):
            for j in range(i+1, k):
                if nums[i] == nums[j]:
                    count += 1
        return count 