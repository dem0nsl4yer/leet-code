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

# Finally solved:

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        k = [0]*n
        t = temperatures 
        stack = []
        for i in range(n):
            while(stack) and temperatures[i] > temperatures[stack[-1]]:
                # looping through the index location 
                prev_idx = stack.pop()
                k[prev_idx] = i- prev_idx
            stack.append(i)
        return k

