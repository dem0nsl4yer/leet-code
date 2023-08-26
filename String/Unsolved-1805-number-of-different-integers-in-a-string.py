class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        word += 'a'
        m = set()
        z = ''
        add = False 
        num = False 
        hold = False 
        for i in range(len(word)):
            if word[i] in arr:
                if word[i] != '0':
                    num = True 
                if num:
                    z += word[i]
                add = True 
            if word[i] not in arr:
                if z =='0':
                    hold = True 
                if z.lstrip('0') and add:
                    k = int(z.lstrip('0'))
                    if k not in m:
                        m.add(k)
                    add = False 
                    z = ''
                    num = False 
        if hold:
            return len(m)+1
        else:
            return len(m)