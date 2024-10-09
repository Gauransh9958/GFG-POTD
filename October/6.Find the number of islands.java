
import java.util.Stack;

class Solution {
    private static final int[] rowDirection = {-1, -1, -1, 0, 0, 1, 1, 1};
    private static final int[] colDirection = {-1, 0, 1, -1, 1, -1, 0, 1};

    private void dfsIterative(char[][] grid, int startRow, int startCol) {
        Stack<int[]> stack = new Stack<>();
        stack.push(new int[]{startRow, startCol});
        grid[startRow][startCol] = '0';

        while (!stack.isEmpty()) {
            int[] cell = stack.pop();
            int row = cell[0], col = cell[1];

            for (int i = 0; i < 8; i++) {
                int newRow = row + rowDirection[i];
                int newCol = col + colDirection[i];

                if (newRow >= 0 && newRow < grid.length && newCol >= 0 && newCol < grid[0].length && grid[newRow][newCol] == '1') {
                    stack.push(new int[]{newRow, newCol});
                    grid[newRow][newCol] = '0';
                }
            }
        }
    }

    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }

        int numIslands = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    dfsIterative(grid, i, j);
                    numIslands++;
                }
            }
        }

        return numIslands;
    }
}