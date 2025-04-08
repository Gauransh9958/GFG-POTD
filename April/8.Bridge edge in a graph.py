class Solution:
    def isBridge(self, V, edges, c, d):
        adj = {i: [] for i in range(V)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        adj[c].remove(d)
        adj[d].remove(c)

        def dfs(v, visited):
            visited[v] = True
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    dfs(neighbor, visited)

        visited = [False] * V
        dfs(c, visited)

        return not visited[d]

