class Solution:
    def minSum(self, arr):
        if len(arr) == 1:
            return str(arr[0])
        
        arr.sort()
        
        num1, num2 = "", ""
        
        for i in range(len(arr)):
            if i % 2 == 0:
                num1 += str(arr[i])
            else:
                num2 += str(arr[i])
        
        def add_strings(str1, str2):
            if len(str1) < len(str2):
                str1, str2 = str2, str1
            
            str1, str2 = str1[::-1], str2[::-1]
            result = []
            carry = 0
            
            for i in range(len(str1)):
                digit1 = int(str1[i])
                digit2 = int(str2[i]) if i < len(str2) else 0
                total = digit1 + digit2 + carry
                result.append(str(total % 10))
                carry = total // 10
            
            if carry:
                result.append(str(carry))
            
            return ''.join(result[::-1])
        
        total_sum = add_strings(num1, num2)
        
        return total_sum.lstrip('0') or '0'