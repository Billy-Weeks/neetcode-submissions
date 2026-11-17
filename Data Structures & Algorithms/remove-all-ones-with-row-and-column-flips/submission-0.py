class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        for row in grid:
            flipped = row[0] ^ grid[0][0]
            for j, value in enumerate(row):
                if value != (grid[0][j] ^ flipped):
                    return False
        return True
