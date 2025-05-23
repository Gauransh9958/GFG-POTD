class Solution:

    def levelOrder(self, root):
        if root is None:
            return []

        q = deque()
        res = []

        q.append(root)
        currLevel = 0

        while q:
            len_q = len(q)
            res.append([])

            for _ in range(len_q):
                node = q.popleft()
                res[currLevel].append(node.data)

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)
            currLevel += 1

        return res
