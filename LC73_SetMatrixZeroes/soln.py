from typing import List


class Solution:
    # Traverse
    # Time Complexity: O(mn)
    # Space Complexity: O(m+n)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return
        n = len(matrix)
        m = len(matrix[0])
        row = set()
        column = set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)
        
        for i in range(n):
            if i in row:
                for j in range(m):
                    matrix[i][j] = 0
        
        for j in range(m):
            if j in column:
                for i in range(n):
                    matrix[i][j] = 0
        