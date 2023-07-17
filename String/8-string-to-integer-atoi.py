class Solution:
    def myAtoi(self, s: str) -> int:
        b = ''
        z = ['+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
        is_negative = False
        is_sign_encountered = False
        is_digit_encountered = False
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Read characters until a non-digit or non-whitespace character is encountered
        for i in s:
            if i in z:
                if i.isdigit():
                    is_sign_encountered = True 
                    is_digit_encountered = True 
                if i == '-':
                    if is_sign_encountered:
                        break
                    is_negative = True
                    is_sign_encountered = True
                elif i == '+':
                    if is_sign_encountered:
                        break
                    is_sign_encountered = True
                elif i == ' ':
                    if is_digit_encountered or is_sign_encountered:
                        break 
                elif i != ' ':
                    if not i.isdigit():
                        break
                    b += i
            else:
                break

        if len(b) == 0:
            return 0

        result = int(b) if not is_negative else -int(b)
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result