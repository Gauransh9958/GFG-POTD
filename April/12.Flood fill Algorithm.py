class Solution:

    def dfs(self, image, x, y, oldColor, newColor):

        if (x < 0 or x >= len(image) or y < 0 or y >= len(image[0])
                or image[x][y] != oldColor):
            return

        image[x][y] = newColor

        self.dfs(image, x + 1, y, oldColor, newColor)
        self.dfs(image, x - 1, y, oldColor, newColor)
        self.dfs(image, x, y + 1, oldColor, newColor)
        self.dfs(image, x, y - 1, oldColor, newColor)

    def floodFill(self, image, sr, sc, newColor):

        if image[sr][sc] == newColor:
            return image

        self.dfs(image, sr, sc, image[sr][sc], newColor)

        return image
