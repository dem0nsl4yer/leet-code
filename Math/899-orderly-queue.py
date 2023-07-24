# Unsolved 


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if len(s)<2:
            return s
        # If k == 1, rotate the string to find the smallest one
        i = count = 0
        while count < k and i < len(s) - 1:
            if s[i] > s[i + 1]:
                m = s[i]
                s = s[:i] + s[i + 1:] + m
                count = 0  # Reset count after each rotation
            else:
                i += 1
                count += 1

        return s
                    