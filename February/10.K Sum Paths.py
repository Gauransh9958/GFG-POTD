class Solution:
    def sumK_util(self, root, sum, cur, mp):
        if root is None:
            return 0

        ans = mp.get(cur + root.data - sum, 0)

        if cur + root.data == sum:
            ans += 1

        mp[cur + root.data] = mp.get(cur + root.data, 0) + 1

        ans += self.sumK_util(root.left, sum, cur + root.data, mp)
        ans += self.sumK_util(root.right, sum, cur + root.data, mp)

        mp[cur + root.data] -= 1

        return ans

    def sumK(self, root, k):
        mp = {}
        return self.sumK_util(root, k, 0, mp)