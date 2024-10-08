
class Solution:
    def multiply_two_lists(self, first, second):
        MOD = 10**9 + 7
        
        def list_to_number(head):
            num = 0
            while head:
                num = (num * 10 + head.data) % MOD
                head = head.next
            return num
        
        num1 = list_to_number(first)
        num2 = list_to_number(second)
        
        result = (num1 * num2) % MOD
        
        return result
