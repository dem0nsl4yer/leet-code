class Solution:
    def isPalindrome(self, x: int) -> bool:
        k = str(x)
        l = len(k)
        if l == 1:
            return True 
        if l % 2 != 0:
            middle = l // 2
            if k[:middle] == k[middle+1:][::-1]:
                return True
            else:
                return False 
        else:
            middle = (l + 1) // 2
            if k[:middle] == k[middle:][::-1]:
                return True
            else:
                return False 