class Solution:
    def isValid(self, arr, k, maxPages):
        students = 1
        current_sum = 0
        
        for pages in arr:
            if pages > maxPages:
                return False
            if current_sum + pages > maxPages:
                students += 1
                current_sum = pages
                if students > k:
                    return False
            else:
                current_sum += pages
        
        return True
    
    def findPages(self, arr, k):
        if k > len(arr):
            return -1
        low, high = max(arr), sum(arr)
        result = high
        
        while low <= high:
            mid = (low + high) // 2
            if self.isValid(arr, k, mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result
