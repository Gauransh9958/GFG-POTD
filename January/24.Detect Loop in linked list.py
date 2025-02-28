

class Solution:
    def detectLoop(self, head):

        slow = head
        fast = head


        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next


            if slow == fast:
                return True

        return False