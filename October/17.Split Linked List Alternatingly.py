class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def alternatingSplitList(self, head):
        if head is None:
            return [None, None]

        head1, head2 = None, None
        tail1, tail2 = None, None
        add_to_first = True
        current = head
        while current:
            if add_to_first:
                if head1 is None:
                    head1 = tail1 = current
                else:
                    tail1.next = current
                    tail1 = tail1.next
            else:
                if head2 is None:
                    head2 = tail2 = current
                else:
                    tail2.next = current
                    tail2 = tail2.next

            add_to_first = not add_to_first
            current = current.next



        # Terminate both lists.
        if tail1:
            tail1.next = None
        if tail2:
            tail2.next = None

        return [head1, head2]
