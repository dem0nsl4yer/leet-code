class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        counter = 0

        # Handle empty strings
        if not s:
            return True
        elif not t:
            return False

        for i in s:
            found = False

            # Iterate through the remaining characters in t
            for j in range(counter, len(t)):
                if i == t[j]:
                    counter = j + 1  # Move the counter to the next position in t
                    found = True
                    break
# Flag usage.
            if not found:
                return False

        return True
        