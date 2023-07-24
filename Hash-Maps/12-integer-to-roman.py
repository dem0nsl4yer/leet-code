class Solution:
    def intToRoman(self, num: int) -> str:
        hm = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        value = ''
        for val, sym in hm.items():
            while(num>=val):
                if num >= val:
                    num -= val
                    value += sym
        return value 
                