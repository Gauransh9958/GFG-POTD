class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sumOfLastN_Nodes(self, head: Node, n: int) -> int:
        if not head:
            return 0

        fast = head
        slow = head

        for _ in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        total_sum = 0
        while slow:
            total_sum += slow.data
            slow = slow.next

        return total_sum
