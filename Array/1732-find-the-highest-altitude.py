class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAl = 0 
        ctr = 0
        for i in gain:
            ctr += i
            maxAl = max(ctr, maxAl)
        return maxAl
        