import turtle
from random import randint
from time import sleep
from turtle import hideturtle

grid = []
grid.append([0, 0, 0, 0, 0, 7, 5, 3, 0])
grid.append([0, 0, 4, 0, 0, 0, 1, 0, 0])
grid.append([3, 8, 0, 6, 0, 0, 0, 0, 7])
grid.append([4, 0, 0, 0, 0, 2, 0, 0, 5])
grid.append([0, 9, 0, 8, 3, 6, 0, 7, 0])
grid.append([0, 1, 0, 0, 0, 0, 0, 9, 0])
grid.append([0, 0, 9, 3, 0, 0, 0, 0, 4])
grid.append([1, 3, 2, 5, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#000000")
myPen.hideturtle()
topLeft_x = -150
topLeft_y = 150

def text(message, x, y, size):
    FONT = ('Arial', size, 'normal')
    myPen.penup()
    myPen.goto(x,y)
    myPen.write(message, align="left", font=FONT)

#A procedure to draw the grid on screen using Python Turtle

def drawGrid(grid):
    intDim = 35
    for row in range(0,10):
        if (row % 3) == 0:
            myPen.pensize(3)
        else:
            myPen.pensize(1)
        myPen.penup()
        myPen.goto(topLeft_x, topLeft_y - row*intDim)
        myPen.pendown()
        myPen.goto(topLeft_x + 9*intDim, topLeft_y - row*intDim)
    for col in range(0,10):
        if (col % 3) == 0:
            myPen.pensize(3)
        else:
            myPen.pensize(1)
        myPen.penup()
        myPen.goto(topLeft_x + col*intDim, topLeft_y)
        myPen.pendown()
        myPen.goto(topLeft_x + col*intDim, topLeft_y - 9*intDim)
    
    for row in range (0,9):
        for col in range (0,9):
            if grid[row][col] != 0:
                text(grid[row][col], topLeft_x + col*intDim+9, topLeft_y - row*intDim - intDim+8, 18)


#A function to check if the grid is full

def checkGrid(grid):
    for row in range(0,9):
        for col in range(0,9):
            if grid[row][col] == 0:
                return False

    return True # We have a complete grid!


#A backtracking/recursive function to check all possible combinations of numbers until a solution is found

def solveGrid(grid):
    #Find next empty cell
    for i in range (0,81):
        row = i // 9
        col = i % 9

        if grid[row][col] == 0:
            for value in range (1, 10):
                #Check that this value has not already been used on this row
                if not (value in grid[row]):
                    #Check that this value has not already been used on this column
                    if not value in (grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col], grid[6][col], grid[6][col], grid[7][col], grid[8][col]):
                        #Identify which of the 9 squares are we working on
                        square = []

                        if row < 3:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(0,3)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(0,3)]
                            else:
                                square = [grid[i][6:9] for i in range(0,3)]
                        elif row < 6:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(3,6)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(3,6)]
                            else:
                                square = [grid[i][6:9] for i in range(3,6)]
                        else:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(6,9)]
                            elif col <6:
                                square = [grid[i][3:6] for i in range(6,9)]
                            else:
                                square = [grid[i][6:9] for i in range(6,9)]
                        #Check that this value has not already been used on this 3x3 square
                        if not value in (square[0] + square[1] + square [2]):
                            grid[row][col] = value
                            if checkGrid(grid):
                                print("Grid Complete and Checked")
                                return True
                            else:
                                if solveGrid(grid):
                                    return True
            break
    print("Backtrack... There is still Hope")
    grid[row][col] = 0


drawGrid(grid)
myPen.getscreen().update()
sleep(1)

text("Solving", -40, 165, 20)
sleep(1)

myPen.speed(1)
text(".", 50, 165, 20)
text(".", 55, 165, 20)
text(".", 60, 165, 20)
solved = solveGrid(grid)

if solved:
    myPen.clear()
    myPen.speed(0)
    drawGrid(grid)
    myPen.getscreen().update()
    print("There is no such thing as Luck!")
    text("Sudoku Grid Solved", -110, -250, 20)
    text("Click on the Grid to continue...", -80, -280, 10)
else:
    print("Cannot Solve Sudoku Grid")
    text("There is no Hope", -130, -190, 20)

#myPen.getscreen().update()
turtle.exitonclick()






#Backtracking Algorithm - Sudoku Solver - www.101computing.net/backtracking-algorithm-sudoku-solver/