from collections import deque

class Solution:
    def bfs(self, adj):
        n = len(adj)
        
        visited = [False] * n
        
        bfs_traversal = []
        
        for start_node in range(n):
            if not visited[start_node]:
                queue = deque([start_node])
                visited[start_node] = True
                
                while queue:
                    node = queue.popleft()
                    bfs_traversal.append(node)
                    
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
        
        return bfs_traversal