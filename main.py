from board import board

def checkrow(board, row):
    '''
    in : 9x9 matrix(list) of int, row index (int)
    proc : checks whether the element introduced in that row,col violates that row, i.e., 
            whether that number in row,col is present in that row
    out : True if does not violates, False if not
    '''
    for i in range(9):
        target = board[row][i]
        if target != 0:
            for j in range(9):
                if j != i and target == board[row][j]:
                    return False
    return True

def checkcol(board, col):
    '''
    in : 9x9 matrix(list) of int, col index (int)
    proc : checks whether the element introduced in that row,col violates that column, i.e., 
            whether that number in row,col is present in that column
    out : True if does not violates, False if not
    '''
    for i in range(9):
        target = board[i][col]
        if target != 0:
            for j in range(9):
                if j != i and target == board[j][col]:
                    return False
    return True

def check3x3(board, row, col):
    '''
    in : 9x9 matrix(list) of int, row index (int), col index (int)
    proc : checks whether the element introduced in that row,col violates that 3x3 square, i.e., 
            whether that number in row,col is present in that 3x3 matrix
    out : True if does not violates, False if not
    '''
    s_row = int(row/3)*3
    e_row = int(row/3)*3 + 3
    s_col = int(col/3)*3
    e_col = int(col/3)*3 + 3
    #Get square as list
    l = []
    for i in range(s_row, e_row):
        for j in range(s_col, e_col):
            l.append(board[i][j])
    #check the list for violation
    for i in range(9):
        target = l[i]
        if target != 0:
            for j in range(9):
                if i != j and target == l[j]:
                    return False
    return True

def checkinserted(board, row, col):
    '''
    in : 9x9 matrix(list) of int, row index (int), col index (int)
    proc : checks whether the element introduced in that row,col violates the rules of sudoku, i.e., the above 3 violations
    out : True if does not violates, False if not
    '''
    return (checkrow(board, row) and checkcol(board, col) and check3x3(board, row, col))

def solve(board):
    '''
    in : 9x9 matrix(list) of int
    proc : fills the element which are '0' according to sudoku rules
    out : true if solvable, false if not
    '''
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for val in range(1, 10):
                    board[row][col] = val
                    if checkinserted(board, row, col) and solve(board):
                        return True
                    board[row][col] = 0
                return False
    return True

def printboard(board):
    '''
    in : 9x9 matrix(list) of int
    proc : prints the board
    out : -
    '''
    print("-----------------")
    for row in range(9):
        for col in range(9):
            print(board[row][col], end=" ")
        print()
    print("-----------------")


print("Before solving")
printboard(board)
if solve(board):
    print("\nAfter solving")
    printboard(board)
else:
    print("Not solvable")
