class Solution:
    def minRemoval(self, intervals):
        intervals.sort(key=lambda x: x[1])
        
        end = intervals[0][1]
        removal_count = 0
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                removal_count += 1
            else:
                end = intervals[i][1]
        
        return removal_count
