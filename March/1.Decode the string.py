
class Solution:
    def decodedString(self, s: str) -> str:
        stack = []
        current_str = ""
        current_num = 0
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append((current_num, current_str))
                current_num = 0
                current_str = ""
            elif char == ']':
                prev_num, prev_str = stack.pop()
                current_str = prev_str + current_str * prev_num
                current_str += char
        
        return current_str
