from typing import List

class Solution:
    
    def dfs(self, adj: List[List[int]]) -> List[int]:
        def dfs_helper(node, visited, result):
            visited[node] = True
            result.append(node)
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs_helper(neighbor, visited, result)
        
        n = len(adj)
        visited = [False] * n
        result = []
        
        for i in range(n):
            if not visited[i]:
                dfs_helper(i, visited, result)
        
        return result

