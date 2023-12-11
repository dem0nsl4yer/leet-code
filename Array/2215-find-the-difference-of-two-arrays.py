class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1 = []
        num2 = []
        for i in nums1:
            if i in nums2:
                continue
            else:
                if i not in num1:
                    num1.append(i)
        for i in nums2:
            if i in nums1:
                continue
            else:
                if i not in num2:
                    num2.append(i)
        return [num1, num2]