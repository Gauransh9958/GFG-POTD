

class Solution:

    def topoSortUtil(self, v, adj, visited, stack):
        visited[v] = True

        for i in adj[v]:
            if not visited[i]:
                self.topoSortUtil(i, adj, visited, stack)

        stack.append(v)

    def topoSort(self, V, edges):
        stack = []
        visited = [False] * V
        adj = [[] for _ in range(V)]

        for it in edges:
            adj[it[0]].append(it[1])

        for i in range(V):
            if not visited[i]:
                self.topoSortUtil(i, adj, visited, stack)

        return stack[::-1]
