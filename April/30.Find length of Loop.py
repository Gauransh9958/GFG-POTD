class Solution:
    def countNodesInLoop(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return self.countLoopLength(slow)

        return 0

    def countLoopLength(self, node_in_loop):
        count = 1
        current = node_in_loop.next
        while current != node_in_loop:
            count += 1
            current = current.next
        return count

