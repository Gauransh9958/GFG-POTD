

class Solution:
    dia = 0

    def util(self, root):

        if root == None:
            return 0
        global dia

        l = self.util(root.left)
        r = self.util(root.right)

        dia = max(dia, l + r + 1)

        return 1 + max(l, r)

    def diameter(self, root):
        global dia
        dia = 0
        self.util(root)
        return dia - 1