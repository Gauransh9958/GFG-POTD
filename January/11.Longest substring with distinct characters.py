class Solution:

    def longestUniqueSubstr(self, s):
        MAX_CHAR = 26
        if len(s) == 0 or len(s) == 1:
            return len(s)

        res = 0
        vis = [False] * MAX_CHAR

        left = 0
        right = 0
        while right < len(s):

            while vis[ord(s[right]) - ord('a')] == True:
                vis[ord(s[left]) - ord('a')] = False
                left += 1

            vis[ord(s[right]) - ord('a')] = True


            res = max(res, (right - left + 1))
            right += 1

        return res