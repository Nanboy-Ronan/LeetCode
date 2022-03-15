import java.util.LinkedList;
import java.util.Queue;


class Solution {
    // BFS
    // Time Complexity: O(n^2)
    // Space Complexity :O(n^2)
    public int maxAreaOfIsland(int[][] grid) {
        int numRow = grid.length;
        int numCol = grid[0].length;
        Queue<Coordinate> queue = new LinkedList<>();
        int[][] directions = { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };
        int result = 0;
        for (int i = 0; i < numRow; i++) {
            for (int j = 0; j < numCol; j++) {
                int counter = 0;
                if (grid[i][j] == 1) {
                    Coordinate p = new Coordinate(i, j);
                    queue.offer(p);
                    while (!queue.isEmpty()) {
                        Coordinate curr = queue.remove();
                        counter++;
                        grid[curr.getX()][curr.getY()] = 0;
                        for (int[] dir : directions) {
                            int x = curr.getX() + dir[0];
                            int y = curr.getY() + dir[1];
                            if (x >= 0 && x < numRow && y >= 0 && y < numCol && grid[x][y] == 1) {
                                grid[x][y] = 0;
                                queue.offer(new Coordinate(x, y));
                            }
                        }

                    }
                    result = result < counter? counter : result;
                }
            }
        }

        return result;
    }

    private class Coordinate {
        private int x;
        private int y;

        public Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return this.x;
        }

        public int getY() {
            return this.y;
        }

        public void setX(int x) {
            this.x = x;
        }

        public void setY(int y) {
            this.y = y;
        }

    }
}