class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def getCount(self, head):
        count = 0
        current = head
        
        while current is not None:
            count += 1
            current = current.next
            
        return count
