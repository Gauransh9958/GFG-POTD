class Solution:

    def countPS(self, s):
        n = len(s)
        res = 0

        dp = [[False] * n for i in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                res += 1


        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap

                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    res += 1

        return res
