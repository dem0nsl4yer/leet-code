class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize two pointers
        i = 0
        j = 0

        # Loop through the array
        while j < len(nums):
            # If the element is non-zero, swap it with the element at i
            if nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            # Move the pointer j regardless of the value
            j += 1
        
