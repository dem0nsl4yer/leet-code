class Solution:
    def longestPalindrome(self, s: str) -> int:
        k = len(s)
        if k < 2:
            return k
        hash = {}
        for i in s:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
        counter = 0 
        odd = False 
        for i in hash:
            if hash[i] % 2 == 0:
                counter += hash[i]
            else:
                # Change: Removed the unnecessary condition "elif hash[i] > 1"
                counter += hash[i] - 1  # Subtract one to make even pairs
                odd = True  # Set odd flag to true for any character with odd count
        if odd:
            return counter + 1  # If any odd-count character present, add one to the counter
        else:
            return counter