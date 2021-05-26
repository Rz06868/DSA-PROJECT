import pygame

pygame.font.init()
width = 1010
height = 660
background_color = (0, 0, 0)
actual_color = (255, 0, 0)
display = pygame.display.set_mode((width, height)) #makes window 
pygame.display.set_caption("SUDOKU SOLVER") #gives title to the window
display.fill(background_color) #fills the background 
font_size = pygame.font.SysFont(None, 32)
font1 = pygame.font.SysFont(None, 28)

# board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0]
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0]]


board = [
    [3, 7, 8, 4, 1, 0, 2, 0, 0],
    [5, 6, 0, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 7, 6, 0, 0, 0, 1],
    [0, 0, 0, 3, 0, 0, 6, 0, 0],
    [0, 3, 2, 1, 0, 0, 8, 9, 0],
    [0, 0, 6, 2, 8, 4, 3, 5, 7],
    [0, 0, 4, 0, 0, 0, 0, 0, 5],
    [0, 5, 0, 0, 3, 1, 9, 4, 6],
    [6, 1, 0, 0, 0, 0, 7, 0, 8]]
#makes the board 

grid = [[board[i][j] for j in range(len(board[0]))] for i in range(len(board))]

# used in the sudoku solver visualiser 
puzzle = [[board[i][j] for j in range(len(board[0]))] for i in range(len(board))]

#used in solved to solve the grid that will be displayed when esc is pressed 
def empty_cell():
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return row, col
    return None, None
#used to find the next empty cells 
def possible(grid, row, column, number):
    for i in range(0, 9): #check if the number is in the row
        if grid[row][i] == number:
            return False

    for i in range(0, 9): #check if the number is in the column
        if grid[i][column] == number:
            return False

    x0 = (row//3)*3 #check if the number is in the box
    y0 = (column//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[x0+i][y0+j] == number:
                return False

    return True

def solve(puzzle):
    row, column = empty_cell()
    if row is None:
        return True

    for number in range(1, 10):
        if possible(puzzle, row, column, number):
            puzzle[row][column] = number
            if solve(puzzle):
                return True
        puzzle[row][column] = 0
    return False
#used to solve the puzzle 
solve(puzzle)

def solve_vis(grid, i, j, display):

    while grid[i][j] != 0: #solve row wise
        if j < 8:
            j += 1
        elif j == 8 and i < 8:
            j = 0
            i += 1
        elif j == 8 and i == 8:
            return True
    for number in range(1, 10):
        if possible(grid, i, j, number) == True:
            grid[i][j] = number
            pygame.draw.rect(display, background_color, ((0), (0), (640), (660)))
            draw_board(display)
            put_numbers(display, font_size, grid)
            instructions()
            pygame.display.update()
            pygame.time.delay(80)
            if solve_vis(grid, i, j, display) == 1:
                return True
            else:
                grid[i][j] = 0
            pygame.draw.rect(display, background_color,((110), (0), (500), (60-10)))
            draw_board(display)
            put_numbers(display, font_size, grid)
            instructions()
            pygame.display.update()
            pygame.time.delay(50)

    text1 = font_size.render("There is no solution possible", True, (255, 0, 0))
    display.blit(text1, (150, 20))
    pygame.display.update()

def insert(display, points):
    i, j = points[1], points[0]
    font_size = pygame.font.SysFont(None, 32)
    run= True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if (grid[i-1][j-1] != 0):
                    pygame.draw.rect(display, background_color,((110), (0), (500), (60-10)))
                    text = font_size.render("Number on original grid: Cannot be replaced", True, (255, 0, 0))
                    display.blit(text, (110, 20))
                    pygame.display.update()
                    return
                if (event.key == 27): #press esc to solve
                    pygame.draw.rect(display, background_color,((110), (0), (500), (60-10)))
                    pygame.draw.rect(display, (background_color), ((60), (60), (540), (540)))
                    draw_board(display)
                    put_numbers(display, font_size, puzzle)
                    return 
                if (event.key == 48): #enter 0 to erase
                    pygame.draw.rect(display, background_color,((110), (0), (500), (60-10)))
                    board[i-1][j-1] = event.key - 48
                    pygame.draw.rect(display, background_color, ((points[0]*60+5), (points[1]*60+5), (60-10), (60-10)))
                    pygame.display.update()
                    return
                if (0 < event.key-48 < 10): #numbers between 0 and 10
                    see = event.key-48  # check using if condition
                    check = False
                    count = 0
                    for k in board:
                        if count == i-1 and see in k:
                            check = True
                        if k[j-1] == see:
                            check = True
                        count = count + 1
                    for k in range(0, 3):
                        for l in range(0, 3):
                            if board[((i-1)//3)*3+k][((j-1)//3)*3+l] == see:
                                check = True
                    if check == True:
                        pygame.draw.rect(display, background_color, ((110), (0), (500), (60-10)))
                        text1 = font_size.render("This number cannot be placed here", True, (255, 0, 0))
                        display.blit(text1, (150, 20))
                        pygame.display.update()
                        return 
                    else:
                        pygame.draw.rect(display, background_color, ((110), (0), (500), (60-10)))
                        pygame.draw.rect(display, background_color, ((points[0]*60+5), (points[1]*60+5), (60-10), (60-10)))
                        input_num = font_size.render(str(event.key-48), True, (0, 255, 0))
                        display.blit(input_num, (points[0]*60+25, points[1]*60+20))
                        board[i-1][j-1] = event.key-48
                        pygame.display.update()
                        return
                if event.key == pygame.K_RETURN: #press enter to visualize
                    solve_vis(grid, 0, 0, display)

        pygame.display.update()

def draw_board(display):
    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(display, (80, 250, 255),(60+60*i, 60), (60+60*i, 600), 5)
            pygame.draw.line(display, (80, 250, 255),(60, 60+60*i), (600, 60+60*i), 5)

        pygame.draw.line(display, (80, 250, 255), (60+60*i, 60), (60+60*i, 600), 2)
        pygame.draw.line(display, (80, 250, 255), (60, 60+60*i), (600, 60+60*i), 2)
    pygame.display.update()
#used to draw the sudoku 
def put_numbers(display, font_size, board):
    for i in range(0, len(board[0])):
        for j in range(0, len(board[0])):
            if (0 < board[i][j] < 10):
                input_num = font_size.render(
                    str(board[i][j]), True, (250, 250, 250))
                display.blit(input_num, ((j+1)*60+25, (i+1)*60+20))
    pygame.display.update()
#used to display the board on the pygame window 
def instructions():
    pygame.draw.rect(display, (250, 250, 250), ((640), (0), (380), (660)))
    text1 = font_size.render("INSTRUCTIONS:", True, (200, 0, 0))
    display.blit(text1, (650, 50))
    tex2 = font1.render("> Enter numbers from 1 to 9,", True, (80, 10, 250))
    display.blit(tex2, (650, 100))
    tex3 = font1.render("> Press '0' to erase your input,", True, (80, 10, 250))
    display.blit(tex3, (650, 130))
    tex5 = font1.render("> Press 'enter' to visualise,", True, (80, 10, 250))
    display.blit(tex5, (650, 160))
    tex6 = font1.render(
        "> Press 'esc' to get the solved sudoku.", True, (80, 10, 250))
    display.blit(tex6, (650, 190))
    pygame.display.update()
#used to display the instructions 
def main():
    draw_board(display)
    put_numbers(display, font_size, board)
    instructions()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                coordinates = pygame.mouse.get_pos()
                print(coordinates)
                insert(display, (coordinates[0]//60, coordinates[1]//60))
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()
