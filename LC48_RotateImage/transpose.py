from typing import List
from numpy import mat

from typing import List


class Solution:
    # Transpose
    # Time Complexity: O(mn)
    # Space Complexity: O(1)
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        numRow = len(matrix)
        numCol = len(matrix[0])
        for i in range(numRow):
            for j in range(i+1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(numRow):
            for j in range(numCol//2):
                 matrix[i][j], matrix[i][numCol - j - 1] = matrix[i][numCol - j - 1],  matrix[i][j]
        