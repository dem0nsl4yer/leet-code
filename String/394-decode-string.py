class Solution:
    def decodeString(self, s: str) -> str:
        nums = '0123456789'
        stack = []
        val = ''
        temp = ''
        i = 0

        while i < len(s):
            if s[i] in nums:
                num = 0
                while i < len(s) and s[i] in nums:
                    num = num * 10 + int(s[i])
                    i += 1
                stack.append(num)
            elif s[i] == '[':
                stack.append(val)
                val = ''
                i += 1
            elif s[i] == ']':
                last_val = stack.pop()
                repeat_times = stack.pop()
                val = last_val + val * repeat_times
                i += 1
            else:
                val += s[i]
                i += 1

        return val