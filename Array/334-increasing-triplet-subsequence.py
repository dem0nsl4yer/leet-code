class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        small = float('inf')  # Initialize small to positive infinity
        big = float('inf')    # Initialize big to positive infinity

        for num in nums:
            if num <= small:
                small = num
            elif num <= big:
                big = num
            else:
                return True

        return False