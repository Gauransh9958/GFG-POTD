class Solution:

    def reverseKGroup(self, head, k):
        if head is None or k == 1:
            return head

        curr = head
        newHead = None
        tail = None

        while curr is not None:
            groupHead = curr
            prev = None
            nextNode = None
            count = 0

            while curr is not None and count < k:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
                count += 1

            if newHead is None:
                newHead = prev

            if tail is not None:
                tail.next = prev

            tail = groupHead

        return newHead