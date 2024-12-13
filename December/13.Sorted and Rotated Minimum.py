class Solution:
    def findMin(self, arr):
        low, high = 0, len(arr) - 1
        
        while low < high:
            mid = (low + high) // 2
            

            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid
        
        return arr[low]
