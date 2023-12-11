# Basic solution. 

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[0:i]) == sum(nums[i+1:]):
                return i 
            else:
                continue 
        return -1 
    
# Less looping. 

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum=0
        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]
        return -1 