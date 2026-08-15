class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
# Check if board is valid sudoku board (numbers 1-9, no repeating)
# input = . means nothing on the board
# thoughts: checking duplicates == using hashset
    # use 3 sep. hash sets to check each guideline at the same time

        # hash sets
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # loop through each cell (only once)
        for row in range(9):
            for col in range(9):
                # First skip "empty" cells (cells with ".")
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rows[row]
                or board[row][col] in cols[col]
                or board[row][col] in squares[(row // 3,
                    col // 3)]):
                    return False
                
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])
        return True



