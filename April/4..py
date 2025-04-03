from collections import deque

class Solution:
    def orangesRotting(self, mat):
        if not mat:
            return 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(mat), len(mat[0])
        
        queue = deque()
        fresh_count = 0
        

        for r in range(rows):