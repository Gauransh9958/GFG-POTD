import heapq

class Solution:
    def nearlySorted(self, arr, k):
        min_heap = []
        
        for i in range(k + 1):
            heapq.heappush(min_heap, arr[i])
        
        index = 0
        
        for i in range(k + 1, len(arr)):
            arr[index] = heapq.heappop(min_heap)
            index += 1
            heapq.heappush(min_heap, arr[i])
        
        while min_heap:
            arr[index] = heapq.heappop(min_heap)
            index += 1

        return arr
