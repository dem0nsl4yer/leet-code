class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        k = [0]*len(temperatures)
        t = temperatures 
        stack = []
        for i in range(len(t)):
            if t[i] < t[i+1]:
                k[i] = 1
            else:
                stack.append(t[i])