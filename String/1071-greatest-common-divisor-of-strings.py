class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        gcd  = ''

        for i in range(1, len2 + 1):
            if len2 % i == 0:
                substr = str2[:i]
                if substr * (len2 // i) == str2 and substr * (len1 // i) == str1:
                    gcd = substr

        return gcd