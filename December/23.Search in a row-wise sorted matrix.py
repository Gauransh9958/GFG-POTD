class Solution:
    
    def searchRowMatrix(self, mat, x):
        for row in mat:
            left, right = 0, len(row) - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == x:
                    return True
                elif row[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
        return False