class Solution:
    def articulationPoints(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        time = [0]
        disc = [-1] * V
        low = [-1] * V
        parent = [-1] * V
        ap = [False] * V
        visited = [False] * V
        
        def dfs(u):
            visited[u] = True
            disc[u] = low[u] = time[0]
            time[0] += 1
            children = 0
            
            for v in adj[u]:
                if not visited[v]:
                    parent[v] = u
                    children += 1
                    dfs(v)
                    
                    low[u] = min(low[u], low[v])
                    
                    if parent[u] == -1 and children > 1:
                        ap[u] = True
                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap[u] = True
                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])
        
        for i in range(V):
            if not visited[i]:
                dfs(i)
        
        result = [i for i in range(V) if ap[i]]
        
        return result if result else [-1]
