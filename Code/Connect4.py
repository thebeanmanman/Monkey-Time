import pygame
from random import randint
pygame.init()
canvas = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) 
canvas_rect = canvas.get_rect()
w_canvas = canvas_rect.right
h_canvas = canvas_rect.bottom
clock = pygame.time.Clock()
pygame.display.set_caption("Tic Tac Time")
current_skin = "Monkey"
def window(background):
    global keys, mouse, mousepos
    if background:
        canvas.fill(background)
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()[0]
    mousepos = pygame.mouse.get_pos()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
def text(text, x, y, si, col, font="jungle adventurer", shadow=False):
    font = pygame.font.SysFont(font,si) 
    if shadow:
        texting = font.render(text, True, "black")
        canvas.blit(texting, (x-texting.get_width()/2+si/30,y+si/30))
    texting = font.render(text, True, col)
    canvas.blit(texting, (x-texting.get_width()/2,y))
def check(x, winc):
            for row in range(len(board)):
                ac_win = 0
                dw_win = 0
                for column in range(len(board)):
                    if board[row][column] == x:
                        ac_win += 1
                    else:
                        ac_win = 0
                    if board[column][row] == x:
                        dw_win += 1
                    else:
                        dw_win = 0
                    if ac_win >= winc or dw_win >= winc:
                        return x
                    
                    if True:
                        for i in range(-1,2,2):
                            di_win = 0
                            try:
                                for r in range(len(board)):
                                    if board[row-r-(1*(bool(i-1)))][column-r*i] == x:
                                        di_win += 1
                                if di_win >= winc:
                                    return x
                            except IndexError:
                                pass
                    
if True:
    opp = 1
    scores = [0,0]
    while True:
        window("white")
        pygame.draw.rect(canvas, "blue", (w_canvas/2-h_canvas/2,0,h_canvas,h_canvas))
        board = []
        for i in range(7):
            sb = []
            for ii in range(7):
                sb.append("")
            board.append(sb)
        turn = randint(0,1)
        can = False
        while True:
            window(False)
            for i in range(1,len(board)):
                pygame.draw.rect(canvas, "black", (w_canvas/2-h_canvas/2,h_canvas/7*i-(h_canvas/36.8)/2,h_canvas,h_canvas/36.8))
                pygame.draw.rect(canvas, "black", (w_canvas/2-h_canvas/2+h_canvas/7*i-(h_canvas/36.8)/2,0,h_canvas/36.8,h_canvas))
            available = 0
            for row in range(len(board)):
                for column in range(len(board)):
                    if board[row][column]:
                        canvas.blit(pygame.transform.scale(pygame.image.load(f"{current_skin}{board[row][column]}.png").convert_alpha(), (h_canvas/7, h_canvas/7)), (w_canvas/2-h_canvas/2+row*h_canvas/7, column*h_canvas/7))
                if mouse or (not opp%2 and not turn%2):
                    if pygame.Rect(w_canvas/2-h_canvas/2+row*h_canvas/7, 0, h_canvas/7, h_canvas).collidepoint(mousepos) or (not opp%2 and not turn%2):
                        if can:
                            for i in range(len(board)):
                                if not board[row][-i-1]:
                                    if turn%2 or opp%2:
                                        board[row][-i-1] = str(turn%2 + 1)
                                        turn += 1    
                                        allow = False
                                    elif allow:
                                        while True:
                                            row = randint(0,len(board)-1)
                                            csn = False
                                            for i in range(len(board)):
                                                if not board[row][-i-1]:
                                                    board[row][-i-1] = str(turn%2 + 1)
                                                    turn += 1
                                                    csn = True
                                                    break
                                            if csn:
                                                break
                                    break
                    if board[row][column]:
                        available += 1
            if mouse:
                if pygame.Rect(w_canvas-100, 0, 100, 100).collidepoint(mousepos) and can:
                    break 
                if pygame.Rect(w_canvas-100, h_canvas-100, 100, 100).collidepoint(mousepos) and can:
                    opp += 1 
                can = False
            else:
                can = True
            pygame.draw.rect(canvas, "green", (w_canvas-100, 0, 100, 100))
            text("#", w_canvas-50, -20, 200, "black")
            pygame.draw.rect(canvas, "red", (w_canvas-100, h_canvas-100, 100, 100))
            text(f"{opp%2+1}", w_canvas-50, h_canvas-100, 200, "black")
            text(str(scores[0]), 150, h_canvas/2+200, 200, "black")
            canvas.blit(pygame.image.load(f"{current_skin}1.png"),(75, h_canvas/2,0,0))
            text(str(scores[1]), w_canvas-150, h_canvas/2+200, 200, "black")
            canvas.blit(pygame.image.load(f"{current_skin}2.png"),(w_canvas-225, h_canvas/2,0,0))
            winner = check(str((turn-1)%2+1), 4)
            allow = True
            if winner:
                scores[int(winner)-1] += 1
                break
            elif available == 49:
                break
            pygame.display.update()
            clock.tick(60)