class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        k = []
        if len(nums1) <= len(nums2):
            m = nums1
            n = nums2
        else:
            m = nums2
            n = nums1
        for i in m:
            if i in n and i not in k:
                k.append(i)
                n.remove(i)
        return k 
