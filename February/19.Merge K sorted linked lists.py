import heapq

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        
    def __lt__(self, other):
        return self.data < other.data

class Solution:
    def mergeKLists(self, arr):
        heap = []
        
        for head in arr:
            if head:
                heapq.heappush(heap, head)
        
        dummy = Node(0)
        current = dummy
        
        while heap:
            smallest_node = heapq.heappop(heap)
            
            current.next = smallest_node
            current = current.next
            
            if smallest_node.next:
                heapq.heappush(heap, smallest_node.next)
        
        return dummy.next
