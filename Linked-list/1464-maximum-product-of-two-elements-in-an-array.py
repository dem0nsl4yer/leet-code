class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        num1 = 0
        key = 0 
        num2 = 0 
        for i in range(len(nums)):
            if nums[i] > num1:
                num2 = num1
                num1 = nums[i]
                key = i 
            elif nums[i] > num2 and i != key:
                num2 = nums[i]
        return (num1 - 1) * (num2 - 1)