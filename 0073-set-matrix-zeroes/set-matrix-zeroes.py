class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows, cols = len(matrix), len(matrix[0])
        newZeros = set() # keep track of all the values set to zero

        def setZeros(r, c):
            # change all the values in the row and columns to zeros
            for rowNode in range(rows):
                if matrix[rowNode][c] != 0:
                    newZeros.add((rowNode,c))
                    matrix[rowNode][c] = 0
            for colNode in range(cols):
                if matrix[r][colNode] != 0:
                    newZeros.add((r,colNode))
                    matrix[r][colNode] = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0 and (r,c) not in newZeros:
                    setZeros(r, c)
        print(newZeros)

        