class Solution:
    def isCycle(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(v, visited, parent):
            visited[v] = True
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    if dfs(neighbor, visited, v):
                        return True
                elif parent != neighbor:
                    return True
            return False

        visited = [False] * V
        for i in range(V):
            if not visited[i]:
                if dfs(i, visited, -1):
                    return True

        return False
