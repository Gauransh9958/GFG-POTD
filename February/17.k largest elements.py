import heapq

class Solution:
    def kLargest(self, arr, k):
        min_heap = arr[:k]
        heapq.heapify(min_heap)
        
        for num in arr[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
        
        return sorted(min_heap, reverse=True)

