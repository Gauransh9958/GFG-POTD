'''
	{
		# Node Class
		class Node:
		def __init__(self, data):   # data -> value stored in node
		self.data = data
		self.next = None
	}
'''


class Solution:
    def segregate(self, head):

        zeroD = Node(0)
        oneD = Node(1)
        twoD = Node(2)

        zero = zeroD
        one = oneD
        two = twoD

        curr_node = head
        while curr_node:

            if curr_node.data == 0:
                zero.next = curr_node
                zero = zero.next
            elif curr_node.data == 1:
                one.next = curr_node
                one = one.next
            else:
                two.next = curr_node
                two = two.next
            curr_node = curr_node.next

        if oneD.next:
            zero.next = oneD.next
        else:
            zero.next = twoD.next
        one.next = twoD.next
        two.next = None

        return zeroD.next
