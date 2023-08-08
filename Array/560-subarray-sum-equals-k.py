class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        start =counter = total = end = 0 
        while(start < len(nums)):
            if end <len(nums):
                total += nums[end]
            if total == k:
                counter += 1

            while(k < total and start <= end):
                total -= nums[start]
                start += 1 
            end +=1 
        return counter 
    
#   Does not works/ 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        start = counter = total = 0 
        end = 0
        
        while end < len(nums):
            total += nums[end]
            
            while total > k and start <= end:
                total -= nums[start]
                start += 1
            
            if total == k:
                counter += 1
            
            end += 1 
        
        return counter

#   Does not works again. 
