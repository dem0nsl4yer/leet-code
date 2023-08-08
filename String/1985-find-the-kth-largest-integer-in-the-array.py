class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums_int = sorted([int(num) for num in nums], reverse = True)
        return str(nums_int[k-1])