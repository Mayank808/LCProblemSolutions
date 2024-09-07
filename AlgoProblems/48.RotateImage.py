class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def transpose(matrix):
            cols = 1
            for row in range(len(matrix)):
                for col in range(cols):
                    matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
                
                cols += 1
            

        def flipOnHalf(matrix):
            for row in matrix:
                left = 0
                right = len(row) - 1

                while left < right:
                    row[left], row[right] = row[right], row[left]
                    left += 1
                    right -= 1
        
        transpose(matrix)
        flipOnHalf(matrix)
        return matrix
        
