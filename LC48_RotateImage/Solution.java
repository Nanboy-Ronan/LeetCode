class Solution {
    // Transpose
    // Time Complexity: O(mn)
    // Space Complexity: O(1)
    public void rotate(int[][] matrix) {
        int numRow = matrix.length;
        int numCol = matrix[0].length;
        for(int i = 0; i < numRow; i++){
            for(int j = i + 1; j < numCol; j++){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        for (int i = 0; i < numRow; i++){
            for(int j = 0; j < numRow / 2; j++){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][numRow - 1 - j];
                matrix[i][numRow - 1 - j] = temp;
            }
        }
    }
}