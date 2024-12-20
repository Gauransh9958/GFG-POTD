class Solution:
    def spirallyTraverse(self, mat):
        if not mat or not mat[0]:
            return []
        
        n, m = len(mat), len(mat[0])
        top, bottom, left, right = 0, n - 1, 0, m - 1
        result = []
        
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                result.append(mat[top][col])
            top += 1
            
            for row in range(top, bottom + 1):
                result.append(mat[row][right])
            right -= 1
            
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(mat[bottom][col])
                bottom -= 1
            
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(mat[row][left])
                left += 1
        
        return result