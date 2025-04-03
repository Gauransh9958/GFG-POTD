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
            for c in range(cols):
                if mat[r][c] == 2:
                    queue.append((r, c, 0))
                elif mat[r][c] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        max_time = 0
        while queue:
            r, c, time = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == 1:
                    mat[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr, nc, time + 1))
                    max_time = max(max_time, time + 1)
        
        if fresh_count > 0:
            return -1
        
        return max_time
