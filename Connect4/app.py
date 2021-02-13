import pygame
import random

#GLOBAR VARS
rows = 7
cols = 8
s_width = 500
s_height = 500

BLACK = (0,0,0)
BLUE = (0,45,186)
WHITE = (255,255,255)
YELLOW = (255,255,0)
RED = (255,0,0)
GREEN = (0,255,0)

circle_radius = 30
board = [[0] * cols for i in range(rows)]
win = pygame.display.set_mode((s_width, s_height))
pygame.font.init()

def draw_board(win):
    for i in range(rows):
        for j in range(cols):
            y_pos = (i*circle_radius+circle_radius + (i*circle_radius) + 75)
            x_pos = (j*circle_radius+circle_radius + (j*circle_radius) + 10)
            if board[i][j] == 0:
                pygame.draw.circle(win, BLACK, (x_pos, y_pos), circle_radius)
            elif board[i][j] == 1:
                pygame.draw.circle(win, YELLOW, (x_pos, y_pos), circle_radius)
            elif board[i][j] == 2:
                pygame.draw.circle(win, RED, (x_pos, y_pos), circle_radius)
            else:
                pygame.draw.circle(win, GREEN, (x_pos, y_pos), circle_radius)


def switch_turn(turn):
    if turn == 1:
        return 2
    else:
        return 1


def insert_on_board(pos_x, turn):
    insertion = 0
    if board[0][pos_x] != 0:
        return turn
    for i in range(rows):
        if board[i][pos_x] == 0:
            insertion = i
    board[insertion][pos_x] = turn
    return switch_turn(turn)


def check_winner(board, turn):
    #Check for horizontal
    for i in range(rows):
        for j in range(cols-3):
            if board[i][j] == turn and board[i][j+1] == turn and board[i][j+2] == turn and board[i][j+3] == turn:
                board[i][j] = board[i][j+1] = board[i][j+2] = board[i][j+3] = 3
                return turn
    #Check for verticals
    for i in range(rows-3):
        for j in range(cols):
            if board[i][j] == turn and board[i+1][j] == turn and board[i+2][j] == turn and board[i+3][j] == turn:
                board[i][j] = board[i+1][j] = board[i+2][j] = board[i+3][j] = 3
                return turn
    #Check for diagonals 1
    for i in range(rows-3):
        for j in range(cols-3):
            if board[i][j] == turn and board[i+1][j+1] == turn and board[i+2][j+2] == turn and board[i+3][j+3] == turn:
                board[i][j] = board[i+1][j+1] = board[i+2][j+2] = board[i+3][j+3] = 3
                return turn
    #Check for diagonals 2
    for i in range(rows-3):
        for j in range(cols-1, 2, -1):
            if board[i][j] == turn and board[i+1][j-1] == turn and board[i+2][j-2] == turn and board[i+3][j-3] == turn:
                board[i][j] = board[i+1][j-1] = board[i+2][j-2] = board[i+3][j-3] = 3
                return turn
    return -1


def main():
    global board
    run = True
    player_pos = 0
    turn = 1
    winner = -1
    while run:
        win.fill(BLUE, (0,70,s_width,s_height))
        win.fill(BLACK, (0,0, s_width, 70))
        draw_board(win)

        if turn == 1:
            pygame.draw.circle(win, YELLOW, (40 + (player_pos*60),35), circle_radius)
        else:
            pygame.draw.circle(win, RED, (40 + (player_pos*60),35), circle_radius)
        
        if winner != -1:
            font = pygame.font.SysFont('comicsans', 70)
            winner_text = font.render(f"Player {switch_turn(turn)}  win!", 1, WHITE)
            win.blit(winner_text, (s_width/2 - 150, s_height/2))   

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and player_pos < 7:
                    player_pos += 1
                if event.key == pygame.K_LEFT and player_pos > 0:
                    player_pos -= 1
                if event.key == pygame.K_RETURN:
                    if winner != -1:
                        player_pos = 0
                        turn = 1
                        board = [[0] * cols for i in range(rows)]
                        winner = -1
                    else:
                        turn = insert_on_board(player_pos, turn)
                        winner = check_winner(board, switch_turn(turn))
                 
    pygame.display.quit()


main()