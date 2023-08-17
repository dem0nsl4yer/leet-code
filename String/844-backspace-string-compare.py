class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_b = []
        t_b = []
        for i in s:
            if i == '#':
                if s_b:
                    s_b.pop()
            else:
                s_b.append(i)
        for i in t:
            if i == '#':
                if t_b:
                    t_b.pop() 
            else:
                t_b.append(i)
        return s_b == t_b