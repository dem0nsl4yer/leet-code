class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        stack = []
        for i in arr:
            if 2*i in stack:
                return True
            elif i%2 == 0 and i/2 in stack:
                return True 
            else:
                stack.append(i)
        return False 