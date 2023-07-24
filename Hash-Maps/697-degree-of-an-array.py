class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        k = {}
        left = {}
        right = {}
        for i,num in enumerate(nums):
            if num in k:
                k[num] += 1 
                right[num] = i 
            else:
                k[num] = 1
                left[num] = i 
                right[num] = i 

        degree = max(k.values())
        min_len = len(nums)

        for num, freq in k.items():
            if freq == degree:
                min_len = min(min_len, right[num] -left[num] + 1)
        return min_len