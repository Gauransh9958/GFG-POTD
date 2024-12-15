class Solution:
    def peakElement(self, arr):
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Check if mid is a peak element
            if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]):
                return mid
            # If the left neighbor is greater, peak must be in the left half
            elif mid > 0 and arr[mid - 1] > arr[mid]:
                right = mid - 1
            # If the right neighbor is greater, peak must be in the right half
            else:
                left = mid + 1
        
        return -1  # This should never be reached because the array has at least one peak.
