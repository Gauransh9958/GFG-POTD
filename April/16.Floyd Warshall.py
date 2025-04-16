class Solution:

    def floydWarshall(self, dist):
        V = len(dist)


        for k in range(V):

            for i in range(V):


                for j in range(V):


                    if dist[i][k] != 100000000 and dist[k][
                            j] != 100000000 and dist[i][
                                j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
