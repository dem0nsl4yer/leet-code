class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lis = []
        t = len(nums)//2 
        for i in range(t):
            lis.append(nums[i])
            lis.append(nums[i+t])
        return lis