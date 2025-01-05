class Solution:
    def countPairs(self, arr, target):
        arr.sort()
        count = 0
        left = 0
        right = len(arr) - 1
        while left < right:
            if arr[left] + arr[right] < target:
                count += (right - left)
                left += 1
            else:
                right -= 1
        return count