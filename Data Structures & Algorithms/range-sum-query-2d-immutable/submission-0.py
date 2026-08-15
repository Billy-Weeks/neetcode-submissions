class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # set up list of list
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        # intialize result variable (for summing)
        result_sum = 0
        # iterate through rows given
        for row in range(row1, row2 + 1):
            # iterate through columns chosen of said row
            for col in range(col1, col2 + 1):
                # add integer at that point to sum
                result_sum += self.matrix[row][col]
        return result_sum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)