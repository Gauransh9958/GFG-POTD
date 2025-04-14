class Solution:

    @staticmethod
    def findOrder(words):
        cycle_exist = False
        ans = []
        exist = [False] * 2
        vis = [False] * 26
        rec = [False] * 26
        graph = [[0] * 26 for _ in range(26)]

        def dfs(u):
            nonlocal cycle_exist
            vis[u] = rec[
                u] = True
            for v in range(26):
                if graph[u][v] and not vis[
                        v]: 
                    dfs(v)
                elif graph[u][v] and rec[v]:
                    cycle_exist = True
            ans.append(chr(ord('a') + u))
            rec[u] = False 

        for word in words:
            for ch in word:
                exist[ord(ch) - ord('a')] = True

        for i in range(len(words) - 1):
            a, b = words[i], words[i + 1]
            n, m, ind = len(a), len(b), 0
            while ind < n and ind < m and a[ind] == b[ind]:
                ind += 1
            if ind != n and ind == m: 
                return ""
            if ind < n and ind < m: 
                graph[ord(a[ind]) - ord('a')][ord(b[ind]) - ord('a')] = 1

        for i in range(26):
            if exist[i] and not vis[i]:
                dfs(i)

        if cycle_exist: 
            return ""

        return "".join(
            reversed(ans)) 