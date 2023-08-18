class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        m = tickets
        sec = 0
        for i in range(len(m)):
            sec += min(m[i], m[k])
            if i >k and m[i] >= m[k]:
                sec -= 1
        return sec 
