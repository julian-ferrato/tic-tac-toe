import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS

WHITE = (255, 255, 255)
LINE_COLOR = (23, 145, 135)
BG_COLOR = (28, 170, 156)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')

board = [[None, None, None], [None, None, None], [None, None, None]]

player = "X"

board = [[None]*BOARD_COLS for _ in range(BOARD_ROWS)]

def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

draw_lines()

def check_winner():
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            return True

    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return True

    return False

filled_squares = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            
            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)
            
            if board[clicked_row][clicked_col] is None:
                board[clicked_row][clicked_col] = player
                filled_squares += 1
                
                if check_winner():
                    print(f"Le joueur {player} a gagné !")
                    running = False
                elif filled_squares == BOARD_ROWS * BOARD_COLS:
                    print("Match nul !")
                    running = False
                else:
                    if player == "X":
                        player = "O"
                    else:
                        player = "X"
                    
                    print(board)

                    for row in range(BOARD_ROWS):
                        for col in range(BOARD_COLS):
                            if board[row][col] == "X":
                                pygame.draw.line(screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE),
                                                 ((col + 1) * SQUARE_SIZE, (row + 1) * SQUARE_SIZE), 5)
                                pygame.draw.line(screen, WHITE, ((col + 1) * SQUARE_SIZE, row * SQUARE_SIZE),
                                                 (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE), 5)
                            elif board[row][col] == "O":
                                pygame.draw.circle(screen, WHITE, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2),
                                                                   int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                                   int(SQUARE_SIZE // 2 - 5), 2)
                                
                    pygame.display.update()

player = "X"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            
            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)
            
            if board[clicked_row][clicked_col] is None:
                board[clicked_row][clicked_col] = player
                if player == "X":
                    player = "O"
                else:
                    player = "X"
                
                print(board)

                for row in range(BOARD_ROWS):
                    for col in range(BOARD_COLS):
                        if board[row][col] == "X":
                            pygame.draw.line(screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE),
                                             ((col + 1) * SQUARE_SIZE, (row + 1) * SQUARE_SIZE), 5)
                            pygame.draw.line(screen, WHITE, ((col + 1) * SQUARE_SIZE, row * SQUARE_SIZE),
                                             (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE), 5)
                        elif board[row][col] == "O":
                            pygame.draw.circle(screen, WHITE, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2),
                                                               int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                               int(SQUARE_SIZE // 2 - 5), 2)
                            
                pygame.display.update()

pygame.quit()