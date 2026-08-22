# Time to complete: 17 mins

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # row1, col1 == upper left corner
        # row2, col2 == lower right corner 
        # Begin at upper left and make sure we include lower right when iterate

        return_sum = 0
        for row in range(row1, row2 + 1):
            # Controls the rows iteration
            for col in range(col1, col2 + 1):
                # Controls the column iteration
                # Add value at given (row, col) coordinate to sum
                return_sum += self.matrix[row] [col]

        return return_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)