import sys

def constructAdj(V, edges):
    adj = [[] for _ in range(V)]
    for edge in edges:
        u, v, w = edge
        adj[u].append([v, w])
        adj[v].append([u, w])
    return adj

minCycle = sys.maxsize

def dfs(u, parent, adj, visited, path, weights, currWeight):
    global minCycle
    visited[u] = True
    path.append(u)

    for edge in adj[u]:
        v = edge[0]
        w = edge[1]
        if v == parent:
            continue

        if not visited[v]:
            weights.append(w)
            dfs(v, u, adj, visited, path, weights, currWeight + w)
            weights.pop()
        else:
            if v in path:
                idx = path.index(v)
                cycleWeight = sum(weights[idx:]) + w
                minCycle = min(minCycle, cycleWeight)

    path.pop()
    visited[u] = False

def findMinCycle(V, edges):
    global minCycle
    adj = constructAdj(V, edges)
    minCycle = sys.maxsize

    visited = [False] * V
    path = []
    weights = []

    for i in range(V):
        dfs(i, -1, adj, visited, path, weights, 0)

    return minCycle

V = 5
edges = [[0, 1, 2], [1, 2, 2], [1, 3, 1],
        [1, 4, 1], [0, 4, 3], [2, 3, 4]]

result = findMinCycle(V, edges)
print(result)
