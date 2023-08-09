class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        i = ['+', '-']
        k = []

        t = len(nums)
        m = 2**t

        while len(k) < m:
            z = []
            for j in range(t):
                l = random.choice(i)
                z.append(l)
            if z not in k:
                k.append(z)

        count = 0
        for l in k:
            expression = '0'
            for sign, num in zip(l, nums):
                m1 = sign + str(num)
                expression += m1
            if eval(expression) == target:
                count += 1

        return count
    

# Need faster solution. 