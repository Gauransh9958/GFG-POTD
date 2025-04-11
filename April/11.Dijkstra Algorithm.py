class Solution:

    def constructAdj(self, edges, V):

        adj = [[] for _ in range(V)]

        for edge in edges:
            u, v, wt = edge
            adj[u].append([v, wt])
            adj[v].append([u, wt])

        return adj

    def dijkstra(self, V, edges, src):
        adj = self.constructAdj(edges, V)

        pq = []

        dist = [sys.maxsize] * V

        heapq.heappush(pq, [0, src])
        dist[src] = 0

        while pq:
            u = heapq.heappop(pq)[1]

            for x in adj[u]:
                v, weight = x[0], x[1]

                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, [dist[v], v])

        return dist




class Solution:

    def minCost(self, houses):
        n = len(houses)
        g = Graph(n)

        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(houses[i][0] - houses[j][0]) + abs(houses[i][1] -
houses[j][1])
                g.addEdge(i, j, cost)

        return g.kruskalsMST()