class Solution:
    def getMinDiff(self, k, arr):
        arr.sort()
        
        n = len(arr)
        initial_diff = arr[n - 1] - arr[0]
        result = initial_diff
        
        for i in range(1, n):
            max_height = max(arr[i - 1] + k, arr[n - 1] - k)
            min_height = min(arr[0] + k, arr[i] - k)
            
            result = min(result, max_height - min_height)
        
        return result

