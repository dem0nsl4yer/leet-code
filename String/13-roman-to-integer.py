class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = ['CM', 'M', 'CD', 'D', 'XC', 'C', 'XL', 'L', 'IX', 'X', 'IV', 'V', 'I']
        x = [900, 1000, 400, 500, 90, 100, 40, 50, 9, 10, 4, 5, 1]
        count = 0 

        for i in range(len(s)):
            if i <len(s)-1:
                if s[i]+s[i+1] in t:
                    for m in range(len(t)):
                        if s[i] == t[m]:
                            count -= ( 2*x[m])  
            for m in range(len(t)):
                if s[i] == t[m]:
                    count += x[m]
        return count