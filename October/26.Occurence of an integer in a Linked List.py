class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def count(self, head, key):
        count = 0
        current = head
        while current is not None:
            if current.data == key:
                count += 1
            current = current.next
        return count
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(1)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)
    head.next.next.next.next.next = Node(3)
    head.next.next.next.next.next.next = Node(1)

    sol = Solution()

    print(sol.count(head, 1))

    print(sol.count(head, 2))
    print(sol.count(head, 3))
    print(sol.count(head, 4))
