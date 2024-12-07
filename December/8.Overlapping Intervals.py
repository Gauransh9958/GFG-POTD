class Solution:
    def mergeOverlap(self, arr):
        arr.sort(key=lambda x: x[0])
        
        merged_intervals = []
        
        for interval in arr:
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        
        return merged_intervals
