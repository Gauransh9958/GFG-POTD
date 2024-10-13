class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def deleteAlt(self, head):
        if head is None:
            return

        current = head

        while current is not None and current.next is not None:
            current.next = current.next.next
            current = current.next
