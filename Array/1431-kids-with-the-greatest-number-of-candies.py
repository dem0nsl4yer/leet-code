class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        k = []
        great = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= great:
                k.append(True) 
            else:
                k.append(False)
        return k 
        