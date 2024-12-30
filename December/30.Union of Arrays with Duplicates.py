class Solution:
    def findUnion(self, a, b):

        hs = set()

        for x in a:
            hs.add(x)

        for y in b:
            hs.add(y)

        return len(hs)


