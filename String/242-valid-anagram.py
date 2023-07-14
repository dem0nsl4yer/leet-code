class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        k = sorted(s)
        m = sorted(t)
        if k == m:
            return True
        else:
            return False 

#Basic sort & check 

OR 

#Use count and check for every element - {set} function in both strings. 