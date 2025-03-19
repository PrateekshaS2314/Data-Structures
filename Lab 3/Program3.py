class Sudoku: 
    def __init__(self, board): 
        self.board = board 
  
    def is_in_row(self, row, num): 
        return num in self.board[row] 
    def is_in_col(self, col, num): 
      return any(self.board[row][col] == num for row in range(9)) 
    def is_in_grid(self, row, col, num): 
        start_row, start_col = 3 * (row // 3), 3 * (col // 3) 
        return any(self.board[r][c] == num for r in range(start_row, start_row + 3) for c in range(start_col,  start_col + 3)) 
    def print_board(self): 
        for row in self.board: 
            print(" ".join(str(num) if num != 0 else "." for num in row)) 
board = [ 
 [5, 3, 0, 0, 7, 0, 0, 0, 0], 
 [6, 0, 0, 1, 9, 5, 0, 0, 0], 
 [0, 9, 8, 0, 0, 0, 0, 6, 0], 
 [8, 0, 0, 0, 6, 0, 0, 0, 3], 
 [4, 0, 0, 8, 0, 3, 0, 0, 1], 
 [7, 0, 0, 0, 2, 0, 0, 0, 6], 
 [0, 6, 0, 0, 0, 0, 2, 8, 0], 
 [0, 0, 0, 4, 1, 9, 0, 0, 5], 
 [0, 0, 0, 0, 8, 0, 0, 7, 9] 
]

sudoku = Sudoku(board) 
sudoku.print_board() 
# Check for number in row, column, and grid 
row, col, num = 0, 2, 3 
print(f"\nIs {num} in row {row}? {'Yes' if sudoku.is_in_row(row, num) else 'No'}") 
print(f"Is {num} in column {col}? {'Yes' if sudoku.is_in_col(col, num) else 'No'}") 
print(f"Is {num} in grid containing cell ({row}, {col})? {'Yes' if sudoku.is_in_grid(row, col, num) else  'No'}") 
