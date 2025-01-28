class Solution:

    def genPermutations(self, n, curr, cnt, res):

        if len(curr) == n:
            res.append(curr)
            return

        for c, count in cnt.items():
            if count == 0:
                continue

            cnt[c] -= 1

            self.genPermutations(n, curr + c, cnt, res)

            cnt[c] += 1

    def findPermutation(self, s):

        res = []

        cnt = {}

        for c in s:
            cnt[c] = cnt.get(c, 0) + 1

        self.genPermutations(len(s), "", cnt, res)
        return res