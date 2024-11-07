from typing import List

class Solution:
    def findSplit(self, arr: List[int]) -> List[int]:
        result = []
        total_sum = sum(arr)
        
        if total_sum % 3 != 0:
            return [-1, -1]
        
        target = total_sum // 3
        current_sum = 0
        i, j = -1, -1
        
        for index in range(len(arr)):
            current_sum += arr[index]
            if current_sum == target:
                i = index
                break
        
        current_sum = 0
        for index in range(i + 1, len(arr)):
            current_sum += arr[index]
            if current_sum == target:
                j = index
                break
        
        if i != -1 and j != -1 and j < len(arr) - 1:
            return [i, j]
        else:
            return [-1, -1]
