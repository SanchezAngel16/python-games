import pygame

#GLOBAL VARS
s_width = 400
s_height = 400

WHITE = (255,255,255)
BLACK = (0,0,0)

SQUARE_SIZE = s_width/3

win = pygame.display.set_mode((s_width, s_height))
board = [[0] * 3 for i in range(3)]

def draw_board(win, board):
    pygame.draw.line(win, WHITE, (s_width/3, 0), (s_width/3, s_height))
    pygame.draw.line(win, WHITE, ((s_width/3) * 2, 0), ((s_width/3) * 2, s_height))
    pygame.draw.line(win, WHITE, (0, s_height/3), (s_width, s_height/3))
    pygame.draw.line(win, WHITE, (0, (s_height/3) * 2), (s_width, (s_height/3) * 2))
    for i in range(3):
        for j in range(3):
            if board[i][j] == 1:
                pygame.draw.circle(win, WHITE, (int(i*SQUARE_SIZE + (SQUARE_SIZE/2)), int(j*SQUARE_SIZE + (SQUARE_SIZE/2))), int(SQUARE_SIZE/2))
            elif board[i][j] == 2:
                pygame.draw.line(win, WHITE, (i*SQUARE_SIZE, j*SQUARE_SIZE), ((i*SQUARE_SIZE) + SQUARE_SIZE, (j*SQUARE_SIZE) + SQUARE_SIZE))
                pygame.draw.line(win, WHITE, ((i*SQUARE_SIZE) + SQUARE_SIZE,j*SQUARE_SIZE), ((i*SQUARE_SIZE), (j*SQUARE_SIZE) + SQUARE_SIZE))


def make_move(pos, turn):
    if pos[0] > 0 and pos[0] < SQUARE_SIZE:
        if pos[1] > 0 and pos[1] < SQUARE_SIZE:
            x = 0
            y = 0
        elif pos[1] > SQUARE_SIZE and pos[1] < SQUARE_SIZE * 2:
            x = 0
            y = 1
        else:
            x = 0 
            y = 2
    elif pos[0] > SQUARE_SIZE and pos[0] < SQUARE_SIZE * 2:
        if pos[1] > 0 and pos[1] < SQUARE_SIZE:
            x = 1
            y = 0
        elif pos[1] > SQUARE_SIZE and pos[1] < SQUARE_SIZE * 2:
            x = 1
            y = 1
        else:
            x =  1
            y = 2
    else:
        if pos[1] > 0 and pos[1] < SQUARE_SIZE:
            x = 2
            y = 0
        elif pos[1] > SQUARE_SIZE and pos[1] < SQUARE_SIZE * 2:
            x = 2
            y = 1
        else:
            x = y = 2
    if board[x][y] == 0:
        board[x][y] = turn


def switch_turn(turn):
    if turn == 1:
        return 2
    return 1


def check_winner(board, turn):
    for i in range(3):
        if board[i][0] == turn and board[i][1] == turn and board[i][2] == turn:
            return True
    for i in range(3):
        if board[0][i] == turn and board[1][i] == turn and board[2][i] == turn:
            return True
    if board[0][0] == turn and board[1][1] == turn and board[2][2] == turn:
        return True
    if board[2][0] == turn and board[1][1] == turn and board[0][2] == turn:
        return True
    return False

def main():
    run = True
    game_over = False
    turn = 2
    while run:
        win.fill(BLACK)
        draw_board(win, board)
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not game_over:
                    make_move(pos, turn)
                    if check_winner(board, turn):
                        print("Ganador: " + str(turn))
                        game_over = True
                    turn = switch_turn(turn)
            if event.type == pygame.KEYDOWN:
                if game_over:
                    game_over = False
                    for i in range(3):
                        for j in range(3):
                            board[i][j] = 0
                

    pygame.display.quit()

main()