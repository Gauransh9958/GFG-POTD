
class Solution:
    def insertInterval(self, intervals, newInterval):
        result = []
        start, end = newInterval
        
        while intervals and intervals[0][1] < start:
            result.append(intervals.pop(0))
        
        while intervals and intervals[0][0] <= end:
            start = min(start, intervals[0][0])
            end = max(end, intervals[0][1])
            intervals.pop(0)
        
        result.append([start, end])
        
        result.extend(intervals)
        
        return result