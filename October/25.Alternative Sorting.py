class Solution:
    def alternateSort(self, arr):
        arr.sort()
        
        n = len(arr)
        result = []
        
        left, right = 0, n - 1
        while left <= right:
            if left != right:
                result.append(arr[right])
            result.append(arr[left])

            left += 1
            right -= 1
        
        return result