import sys

sys.setrecursionlimit(10**6)


class Solution:

    def areAnagrams(self, str1, str2):

        mp = {}

        for i in str1:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1

        for i in str2:
            if i not in mp:
                return False
            else:
                mp[i] -= 1

        for i in mp:
            if mp[i] != 0:
                return False

        return True