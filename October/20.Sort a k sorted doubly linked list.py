import heapq

class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Solution:
    def sortAKSortedDLL(self, head, k):
        if not head:
            return head

        min_heap = []

        curr = head
        for _ in range(k + 1):
            if curr:
                heapq.heappush(min_heap, (curr.data, curr))
                curr = curr.next

        new_head = None
        last = None

        while min_heap:
            _, min_node = heapq.heappop(min_heap)

            if new_head is None:
                new_head = min_node
                new_head.prev = None
                last = new_head
            else:
                last.next = min_node
                min_node.prev = last
                last = min_node

            if curr:
                heapq.heappush(min_heap, (curr.data, curr))
                curr = curr.next

        last.next = None

        return new_head

def print_list(head):
    while head:
        print(head.data, end=" <-> " if head.next else "\n")
        head = head.next

head = DLLNode(3)
head.next = DLLNode(2)
head.next.prev = head
head.next.next = DLLNode(1)
head.next.next.prev = head.next
head.next.next.next = DLLNode(5)
head.next.next.next.prev = head.next.next
head.next.next.next.next = DLLNode(6)
head.next.next.next.next.prev = head.next.next.next
head.next.next.next.next.next = DLLNode(4)
head.next.next.next.next.next.prev = head.next.next.next.next

solution = Solution()
sorted_head = solution.sortAKSortedDLL(head, 2)
print_list(sorted_head)
