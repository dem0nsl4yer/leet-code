class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        z = []
        m = []
        count = 1 
        while(m != target):
            z.append('Push')
            if count in target:
                m.append(count)
            else:
                z.append('Pop')
            count += 1
        return z