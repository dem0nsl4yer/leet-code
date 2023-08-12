class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        k = [-1]*len(nums1)
        for i in range(len(nums1)):
            record = False 
            for j in nums2:
                if nums1[i] == j:
                    record = True
                if record == True:
                    if nums1[i] <j:
                        k[i] = j 
                        break 
        return k 

# Solution 2
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mapp = {}
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                mapp[stack.pop()] = nums2[i]
            stack.append(nums2[i])

        result = [-1]*len(nums1)

        for i, num in enumerate(nums1):
            if num in mapp:
                result[i] = mapp[num]

        return result


#Unsucessful attempt: 

