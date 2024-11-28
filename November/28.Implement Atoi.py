class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        if not s:
            return 0
        
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        result = 0
        for i in range(len(s)):
            if s[i].isdigit():
                result = result * 10 + int(s[i])
            else:
                break

        result *= sign

        INT_MAX = 2147483647
        INT_MIN = -2147483648

        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        
        return result