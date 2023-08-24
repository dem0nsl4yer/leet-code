class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = list(range(1, n+1))

        for num in nums:
            if num in arr:
                arr.remove(num)

            else: 
                duplicate = num
            missing = arr[0]

        return [duplicate, missing]