
def sudoku(board):
    def  is_valid(board, row,column, num):
        for i in range(9):
            if board[row][i] == num:
                return False
            
        #Check Column
        for i in range(9):
            if board[i][column] == num:
                return False
        #Check 3*3 box
        start_row = row//3 *3
        start_column = column//3*3

        for i in range(3):
            for j in range(3):
                if board[start_row + i] [start_column + j] == num:
                    return False
        return True

    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in '123456789':
                        if is_valid(board, i , j , num):
                            board[i][j] = num
                            if solve():
                                return True
                            board[i][j]= '.' # Backtracking
                    return False
        return True
    solve()


board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]

sudoku(board)

for row in board:
    print(row)                        
               
    