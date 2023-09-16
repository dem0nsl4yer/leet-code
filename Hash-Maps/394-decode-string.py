class Solution:
    def decodeString(self, s: str) -> str:
        ans = ''
        temp = ''
        temp_n = ''
        st = []
        st_n = []
        num = '1234567890'

        for char in s:
            if char in num:
                temp_n += char
            elif char == '[':
                st_n.append(temp_n)
                temp_n = ''
                st.append(temp)
                temp = ''
            elif char == ']':
                last_str = st.pop()
                repeat_count = int(st_n.pop())
                temp = last_str + temp * repeat_count
            else:
                temp += char

        return temp


# Cleaner stack-based solution 

class Solution:
    def decodeString(self, s: str) -> str:
        ans_stack = []
        count_stack = []
        current_str = ''
        current_count = 0

        for char in s:
            if char.isdigit():
                current_count = current_count * 10 + int(char)
            elif char == '[':
                count_stack.append(current_count)
                current_count = 0
                ans_stack.append(current_str)
                current_str = ''
            elif char == ']':
                last_str = ans_stack.pop()
                repeat_count = count_stack.pop()
                current_str = last_str + current_str * repeat_count
            else:
                current_str += char

        return ''.join(ans_stack) + current_str
