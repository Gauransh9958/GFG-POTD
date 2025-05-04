class Solution:

    def findSubString(self, str):
        n = len(str)

        visited = [False] * 26
        distinct = 0

        for i in range(n):
            if visited[ord(str[i]) - ord('a')] == False:
                visited[ord(str[i]) - ord('a')] = True
                distinct += 1

        cur = [0] * 26
        cnt = 0

        ans = n
        start = 0
        for i in range(n):
            cur[ord(str[i]) - ord('a')] += 1

            if cur[ord(str[i]) - ord('a')] == 1:
                cnt += 1
            while cnt == distinct:
                ans = min(ans, i - start + 1)
                cur[ord(str[start]) - ord('a')] -= 1
                if cur[ord(str[start]) - ord('a')] == 0:
                    cnt -= 1
                start += 1
        return ans
