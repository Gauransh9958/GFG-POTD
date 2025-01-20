class Solution:
    # Function to merge two sorted linked lists.
    def sortedMerge(self, head1, head2):
        # Creating a dummy node to hang the result on.
        dummy = Node(0)
        tail = dummy

        # Merge both lists until one becomes empty
        while head1 is not None and head2 is not None:
            if head1.data <= head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        # Attach the remaining nodes of whichever list is not empty
        if head1 is not None:
            tail.next = head1
        else:
            tail.next = head2

        return dummy.next