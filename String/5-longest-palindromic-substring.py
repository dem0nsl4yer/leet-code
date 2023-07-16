class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_s = 0
        k_max = 0
        is_even = False

        for k in range(len(s)):
            l = 0
            while k - l >= 0 and k + l < len(s) and s[k - l] == s[k + l]:
                if l > max_s:
                    max_s = l
                    k_max = k
                    is_even = False
                l += 1

            l = 0
            while k - l >= 0 and k + l + 1 < len(s) and s[k - l] == s[k + l + 1]:
                if l >= max_s:
                    max_s = l
                    k_max = k
                    is_even = True
                l += 1

        if is_even:
            return s[k_max - max_s : k_max + max_s + 2]  # Add 2 for the even-length palindrome
        else:
            return s[k_max - max_s : k_max + max_s + 1]  # Add 1 for the odd-length palindrome