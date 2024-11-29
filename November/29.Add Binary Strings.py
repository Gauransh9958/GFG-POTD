class Solution:
    def addBinary(self, s1, s2):
        num1 = int(s1, 2)
        num2 = int(s2, 2)
        result = num1 + num2
        
        binary_result = bin(result)[2:]
        
        return binary_result