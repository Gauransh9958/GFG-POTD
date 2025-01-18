class Solution:
    def reverseList(self, head):
        if head is None:
            return None
        
        prev = None
        current = head
        
        while current is not None:
            next_node = current.next
            
            current.next = prev
            
            prev = current
            current = next_node

        return prev
