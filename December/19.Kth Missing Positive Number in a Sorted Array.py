class Solution:
    def kthMissing(self, arr, k):
        n = len(arr)
        
        total_missing = arr[-1] - n
        
        if k > total_missing:
            return arr[-1] + (k - total_missing)
        
        for i in range(n):
            missing_count = arr[i] - (i + 1)
            if missing_count >= k:
                return arr[i - 1] + (k - (arr[i - 1] - i)) if i > 0 else k
        
        return -1