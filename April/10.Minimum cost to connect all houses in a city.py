class DSU:

    def __init__(self, n):
        self.parent = [-1] * n
        self.rank = [1] * n

    def find(self, i):
        if self.parent[i] == -1:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)

        if s1 != s2:
            if self.rank[s1] < self.rank[s2]:
                self.parent[s1] = s2
            elif self.rank[s1] > self.rank[s2]:
                self.parent[s2] = s1
            else:
                self.parent[s2] = s1
                self.rank[s1] += 1


class Graph:

    def __init__(self, V):
        self.V = V
        self.edgelist = []

    def addEdge(self, x, y, w):
        self.edgelist.append((w, x, y))

    def kruskalsMST(self):

        self.edgelist.sort()
        s = DSU(self.V)

        ans = 0

        count = 0

        for w, x, y in self.edgelist:

            if s.find(x) != s.find(y):
                s.unite(x, y)
                ans += w
                count += 1

            if count == self.V - 1:
                break

        return ans


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