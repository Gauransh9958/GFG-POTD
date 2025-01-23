class Solution:

    def cloneLinkedList(self, head):
        if not head:
            return None

        curr = head
        while curr:
            new_node = Node(curr.data)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        cloned_head = head.next
        clone = cloned_head
        while clone.next:
            curr.next = curr.next.next
            clone.next = clone.next.next
            curr = curr.next
            clone = clone.next
        curr.next = None
        clone.next = None

        return cloned_head