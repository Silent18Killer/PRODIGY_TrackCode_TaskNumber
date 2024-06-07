"""
    Create a program that solves Sudoku puzzles automatically. The program should take an input grid 
    representing an unsolved Sudoku puzzle and use an algorithm to fill in the missing numbers.

    It should use backtracking or other suitable techniques to explore possible solutions and find 
    the correct arrangement of numbers for the puzzle. Once solved, the program should display the 
    completed Sudoku grid.
"""

def possible(row,column,number):
    global sudoku
    for i in range(0, 9):
        if sudoku[row][i] == number:
            return False
    for i in range(0, 9):
        if sudoku[i][column] == number:
            return False
    
    box_start_row = (row//3) * 3
    box_start_column = (column//3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[box_start_row+i][box_start_column+j] == number:
                return False
    return True

def solve():
    for row in range(0,9):
        for column in range(0,9):
            if sudoku[row][column] == 0:
                for n in range(1, 10):
                    if possible(row,column,n):
                        sudoku[row][column] = n
                        if solve():
                            return True
                        sudoku[row][column] = 0
                return False
    return True

def print_board(sudoku):
    for row in sudoku:
        print("|", *row, "|")

input_grid = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

sudoku = input_grid

if solve():
    print("Sudoku solved successfully:")
    print_board(input_grid)
else:
    print("No solution exists.")
