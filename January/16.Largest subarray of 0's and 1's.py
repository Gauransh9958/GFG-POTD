

class Solution:

    def maxLen(self, arr):
        n = len(arr)
        s = [0] * len(arr)

        if (arr[0] == 0):
            s[0] = -1
        else:
            s[0] = 1

        for i in range(1, len(s)):

            if (arr[i] == 0):
                s[i] = s[i - 1] - 1
            else:
                s[i] = s[i - 1] + 1


        d = dict()

        mx_len = 0

        i = 0

        for j in s:


            if (j == 0):
                mx_len = max(mx_len, i + 1)

            if (d.get(j) != None):
                mx_len = max(mx_len, i - d[j])

            else:
                d[j] = i

            i = i + 1

        return mx_len