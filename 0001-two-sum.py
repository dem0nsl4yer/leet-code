class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hashmap = {i:nums.index(i) for i in nums}
        mem = {}
        for i, x in enumerate(nums):
            if x in mem:
                return [i, mem[x]]
            else:
                mem[target-x] = i  
                