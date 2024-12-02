class Solution:
    def isLengthEven(self, head):
        is_even = True
        
        current = head
        
        while current:
            is_even = not is_even
            current = current.next
        
        return is_even
