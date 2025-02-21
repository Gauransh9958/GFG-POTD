import heapq

class Solution:
    def kClosest(self, points, k):
        max_heap = []
        
        for point in points:
            x, y = point
            distance = x * x + y * y
            heapq.heappush(max_heap, (-distance, point))
            
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        result = [point for _, point in max_heap]
        return result

