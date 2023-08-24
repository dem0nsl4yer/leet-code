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
    
## Efficient solution using sets -deriviative of hashmaps. 

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_set = set()
        missing = duplicate = -1

        for num in nums:
            if num in num_set:
                duplicate = num
            else:
                num_set.add(num)

        for i in range(1, n+1):
            if i not in num_set:
                missing = i 
                break

        return [duplicate, missing]