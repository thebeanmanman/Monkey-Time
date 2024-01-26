import pygame
from random import randint
pygame.init()
canvas = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) 
canvas_rect = canvas.get_rect()
w_canvas = canvas_rect.right
h_canvas = canvas_rect.bottom
clock = pygame.time.Clock()
pygame.display.set_caption("Monkey Time")
hitbox = 0
def window(background):
    global keys, mouse, mousepos, hitbox
    if background:
        canvas.fill(background)
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()[0]
    mousepos = pygame.mouse.get_pos()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    if keys[pygame.K_h]:
        hitbox += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
window(False)
def draw(img, rect):
    canvas.blit(img, rect)
    if hitbox%2:
        pygame.draw.rect(canvas, "red", rect, width=5)
def text(text, x, y, si, col, font="jungle adventurer", shadow=False):
    font = pygame.font.SysFont(font,si) 
    if shadow:
        texting = font.render(text, True, "black")
        canvas.blit(texting, (x-texting.get_width()/2+si/30,y+si/30))
    texting = font.render(text, True, col)
    canvas.blit(texting, (x-texting.get_width()/2,y))
def check(x):
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
                    if (3-row == 3) and (3-column == 3):
                        for i in range(-1,2,2):
                            di_win = 0
                            for r in range(len(board)):
                                if board[row-r-(1*(bool(i-1)))][column-r*i] == x:
                                    di_win += 1
                            if di_win == 3:
                                return x
                    if ac_win == 3 or dw_win == 3:
                        return x
class Player():
    def __init__(self,rect,img):
        self.rect = rect
        self.img = pygame.image.load(img).convert_alpha()
        self.points = 0
        self.playing = 0
        self.m = 1
        self.v = 10
        self.is_jump = False
    def movement(self,moving):
        if moving[0]:
            player.is_jump = True
        if moving[1]:
            self.rect.x -= (10 + self.points*0.1)
        if moving[2]:
            self.rect.x += (10 + self.points*0.1)
back_arrow = pygame.image.load("Arrow.png").convert_alpha()
back_rect = (0,0,100,100)
skins = ["Monkey", "Frog", "Jedi", "Sith", "Avengers", "DC"]
games = ["Tic Tac Toe"]
current_skin = "Monkey"
game_mode = False
startplayer = []
for i in range(8):
    startplayer.append(Player(pygame.Rect(0,0,150,150), f"{current_skin}{i+1}.png"))
class Banana():
    def __init__(self,brandom,pos):
        self.rect = pygame.Rect(pos,0,150,150)
        if brandom == 1:
            self.value = 5
            self.img = pygame.image.load(f"{current_skin} green.png").convert_alpha()
        elif brandom <= 3:
            self.value = -3
            self.img = pygame.image.load(f"{current_skin} brown.png").convert_alpha()
        else:
            self.value = 1
            self.img = pygame.image.load(f"{current_skin} yellow.png").convert_alpha()
opening = True
skin_selection = False
game_selection = False
open_ui = False
running = False
winsc = False
winpoints = 100
while True:
    while opening:
        window("blue")
        text("Monkey Time", w_canvas/2, 50, 300, "white", shadow=True)
        text("(But Better)", w_canvas-200, 250, 50, "white",shadow=True)
        play_rect = pygame.Rect(w_canvas/2 -125, h_canvas/2 - 125, 250, 250)
        pygame.draw.rect(canvas, "green", play_rect)
        pygame.draw.polygon(canvas, "black",[(w_canvas/2 + 100,h_canvas/2),(w_canvas/2 - 100, h_canvas/2 - 100),(w_canvas/2 - 100, h_canvas/2 + 100)])
        pygame.draw.rect(canvas, "black", play_rect, width=5)
        game_rect = pygame.Rect(w_canvas/2-400, h_canvas/2-75, 150, 150)
        draw(pygame.image.load("gameicon.png"), game_rect)
        skin_rect = pygame.Rect(w_canvas-300, h_canvas-300, 150, 150)
        draw(pygame.image.load("skin.png").convert_alpha(), skin_rect)
        if mouse or keys[pygame.K_RETURN]:
            if play_rect.collidepoint(mousepos) or keys[pygame.K_RETURN]:
                opening = False
                open_ui = True
        if mouse:
            if skin_rect.collidepoint(mousepos):
                skin_selection = True
            if game_rect.collidepoint(mousepos):
                game_selection = True
        while skin_selection:
            window("blue")
            draw(back_arrow,back_rect)
            if mouse:
                if pygame.Rect(back_rect).collidepoint(mousepos):
                    skin_selection = False
            for skin in skins:
                skin_rect = pygame.Rect(w_canvas/5*(((skins.index(skin))%4)+1)-75,250+200*int(skins.index(skin)/4),150,150)
                text(skin, skin_rect.centerx, skin_rect.y+160, 50, "white", shadow=True)
                if skin == current_skin:
                    pygame.draw.rect(canvas, "green", skin_rect)
                else:
                    pygame.draw.rect(canvas, "orange", skin_rect)
                draw(pygame.image.load(f"{skin}1.png").convert_alpha(), skin_rect)
                if mouse:
                    if skin_rect.collidepoint(mousepos):
                        current_skin = skin
            text("Skin Selection", w_canvas/2, 50, 200, "white", shadow=True)
            pygame.display.update()
            clock.tick(60)
        while game_selection:
            window("blue")
            draw(back_arrow,back_rect)
            if mouse:
                if pygame.Rect(back_rect).collidepoint(mousepos):
                    game_selection = False
            for game in games:
                game_rect = pygame.Rect(w_canvas/5*(((games.index(game))%4)+1)-75,250+200*int(games.index(game)/4),150,150)
                text(game, game_rect.centerx, game_rect.y+160, 50, "white", shadow=True)
                draw(pygame.image.load(f"{game}.png").convert_alpha(), game_rect)
                if mouse:
                    if game_rect.collidepoint(mousepos):
                        game_mode = game
                        game_selection = False
                        opening = False
            text("Game Selection", w_canvas/2, 50, 200, "white", shadow=True)
            pygame.display.update()
            clock.tick(60)
        pygame.display.update()
        clock.tick(60)
    can = True
    for i in startplayer:
        i.img = pygame.image.load(f"{current_skin}{startplayer.index(i)+1}.png").convert_alpha()
    while open_ui:
        window("black")
        text(f"Win Points: {winpoints}", w_canvas/2, 50, 200, "white")
        draw(back_arrow,back_rect)
        if mouse:
                if pygame.Rect(back_rect).collidepoint(mousepos):
                    open_ui = False
                    opening = True
        for i in range(1,6):
            pygame.draw.rect(canvas, "orange", (w_canvas*i/6-100,h_canvas-150,100,100))
            if i == 5:
                if winpoints%50:
                    pygame.draw.rect(canvas, "green", (w_canvas*i/6-100,h_canvas-150,100,100))
                text("RND", w_canvas*i/6-50, h_canvas-112.5, 50, "black")
                if mouse:
                    if pygame.Rect(w_canvas*i/6-100,h_canvas-150,100,100).collidepoint(mousepos) and can:
                        winpoints = randint(50,200)
                        pygame.time.delay(100)
                        can = False
                else:
                    can = True
            else:
                if i*50 == winpoints:
                    pygame.draw.rect(canvas, "green", (w_canvas*i/6-100,h_canvas-150,100,100))
                text(str(i*50), w_canvas*i/6-50, h_canvas-112.5, 50, "black")
                if mouse:
                    if pygame.Rect(w_canvas*i/6-100,h_canvas-150,100,100).collidepoint(mousepos):
                        winpoints = i*50
        canstart = 0
        for i in startplayer:
            canstart += i.playing%2
        if canstart >= 2:
            draw(pygame.transform.rotate(back_arrow,180),(w_canvas-150,h_canvas-150,100,100))
            if mouse or keys[pygame.K_RETURN]:
                if pygame.Rect(w_canvas-150,h_canvas-150,100,100).collidepoint(mousepos) or keys[pygame.K_RETURN]:
                    open_ui = False
        for startplay in startplayer:
            startplay.rect.x = ((startplayer.index(startplay))%4+1)*w_canvas/5-50
            startplay.rect.y = (int(startplayer.index(startplay)/4))*250+200
            draw(startplay.img,startplay.rect)
            if mouse:
                if pygame.Rect(((startplayer.index(startplay))%4+1)*w_canvas/5-50,(int(startplayer.index(startplay)/4))*250+200,150,150).collidepoint(mousepos):
                    if can:
                        startplay.playing += 1
                        can = False
            else:
                can = True
            if startplay.playing%2:
                pygame.draw.rect(canvas, "green", (startplay.rect.x,startplay.rect.bottom,150,50))
                text("Playing", startplay.rect.centerx, startplay.rect.bottom+12.5, 50, "black")
            else:
                pygame.draw.rect(canvas, "orange", (startplay.rect.x,startplay.rect.bottom,150,50))
                text("Not Playing", startplay.rect.centerx, startplay.rect.bottom+12.5, 36, "black")
        pygame.display.update()
        clock.tick(60)
    if not (opening or game_mode):
        running = True
        pausing = False
        players = []
        bananas = []
        for startplay in startplayer:
            if startplay.playing%2:
                players.append(startplay)
        for player in players:
            player.rect.x = ((players.index(player))+1)*w_canvas/(len(players)+1)-50
            player.rect.y = h_canvas-350
    while running:
        window(False)
        canvas.blit(pygame.transform.scale(pygame.image.load(f"{current_skin} sky.jpg").convert_alpha(), (w_canvas, h_canvas)), (0,0))
        canvas.blit(pygame.transform.scale(pygame.image.load(f"{current_skin} grass.jpg").convert_alpha(), (w_canvas, 250)), (0,h_canvas-250))
        pygame.draw.rect(canvas, "black", (0,0,w_canvas,150))
        text(f"Goal: {winpoints}", w_canvas/2, 50, 100, "white")
        if len(bananas) < 5:
            bananas.append(Banana(randint(1,10),randint(0,w_canvas-150)))
        for banana in bananas:
            draw(banana.img,banana.rect)
            banana.rect.y += 10
            if banana.rect.y >= h_canvas:
                bananas.remove(banana)
        controls = [[keys[pygame.K_w], keys[pygame.K_a], keys[pygame.K_d]],[keys[pygame.K_i], keys[pygame.K_j], keys[pygame.K_l]],[keys[pygame.K_g], keys[pygame.K_v], keys[pygame.K_b]],[keys[pygame.K_UP], keys[pygame.K_LEFT], keys[pygame.K_RIGHT]],[keys[pygame.K_2], keys[pygame.K_1], keys[pygame.K_3]],[keys[pygame.K_5], keys[pygame.K_4], keys[pygame.K_6]],[keys[pygame.K_8], keys[pygame.K_7], keys[pygame.K_9]],[keys[pygame.K_MINUS], keys[pygame.K_0], keys[pygame.K_EQUALS]]]
        for player in players:
            draw(player.img,player.rect)
            text(f"Player {startplayer.index(player)+1}: {player.points}", player.rect.centerx, 110, 50, "white")
            player.movement(controls[startplayer.index(player)])
            if player.is_jump:
                F1 =(1 / 2)*player.m*(player.v**2)
                player.rect.y -= F1
                player.v -= 1
                if player.v<0:
                    player.m =-1
                if player.v ==-11:
                    player.is_jump = False
                    player.v = 10
                    player.m = 1
            if player.rect.y > h_canvas-350:
                player.rect.y = h_canvas-350
            player.rect.clamp_ip(canvas_rect)
            if player.points >= winpoints:
                winner = f"Player {startplayer.index(player)+1}"
                running = False
            for banana in bananas:
                if pygame.Rect.colliderect(player.rect, banana.rect):
                    player.points += banana.value
                    bananas.remove(banana)
            if keys[pygame.K_SPACE]: 
                if can:
                    pausing = True
                    can = False
            else:
                can = True
            while pausing:
                window(False)
                pygame.draw.rect(canvas, "black", (w_canvas/2-300, h_canvas/2-300, 600, 600))
                pygame.draw.rect(canvas, "white", (w_canvas/2-150, h_canvas/2-200, 100, 400))
                pygame.draw.rect(canvas, "white", (w_canvas/2+50, h_canvas/2-200, 100, 400))
                if keys[pygame.K_SPACE]: 
                    if can:
                        pausing = False
                        can = False
                else:
                    can = True
                pygame.display.update()
                clock.tick(60)
        pygame.display.update()
        clock.tick(60)
    if not (opening or game_mode):
        winsc = True
        nana_rain = 0
        for startplay in startplayer:
            startplay.points = 0
    while winsc:
        window("yellow")
        nana_rain += 1
        if nana_rain >= 60:
            bananas.append(Banana(randint(1,10),randint(0,w_canvas-150)))
            nana_rain = 0
        for banana in bananas:
            draw(banana.img,banana.rect)
            banana.rect.y += 10
            if banana.rect.y >= h_canvas:
                bananas.remove(banana)
        text(f"Winner: {winner}", w_canvas/2, 100, 200, "black")
        play_rect = pygame.Rect(w_canvas/2 -125, h_canvas/2 - 125, 250, 250)
        pygame.draw.rect(canvas, "green", play_rect)
        pygame.draw.polygon(canvas, "black",[(w_canvas/2 + 100,h_canvas/2),(w_canvas/2 - 100, h_canvas/2 - 100),(w_canvas/2 - 100, h_canvas/2 + 100)])
        pygame.draw.rect(canvas, "black", play_rect, width=5)
        if mouse or keys[pygame.K_RETURN]:
            if play_rect.collidepoint(mousepos) or keys[pygame.K_RETURN]:
                winsc = False
                open_ui = True
        pygame.display.update()
        clock.tick(60)
    opp = 1
    scores = [0,0]
    while game_mode == "Tic Tac Toe":
        window("white")
        draw(back_arrow,back_rect)
        pygame.draw.rect(canvas, "blue", (w_canvas/2-h_canvas/2,0,h_canvas,h_canvas))
        board = [["","",""],["","",""],["","",""]]
        turn = randint(0,1)
        can = False
        while True:
            window(False)
            for i in range(1,3):
                pygame.draw.rect(canvas, "black", (w_canvas/2-h_canvas/2,h_canvas/3*i-(h_canvas/18.4)/2,h_canvas,h_canvas/18.4))
                pygame.draw.rect(canvas, "black", (w_canvas/2-h_canvas/2+h_canvas/3*i-(h_canvas/18.4)/2,0,h_canvas/18.4,h_canvas))
            available = 0
            for row in range(len(board)):
                for column in range(len(board)):
                    if board[row][column]:
                        canvas.blit(pygame.image.load(f"{current_skin}{board[row][column]}.png"),(w_canvas/2-h_canvas/2+row*h_canvas/3+75, column*h_canvas/3+75, h_canvas/3, h_canvas/3))
                    if mouse or (not opp%2 and not turn%2):
                        if pygame.Rect(w_canvas/2-h_canvas/2+row*h_canvas/3, column*h_canvas/3, h_canvas/3, h_canvas/3).collidepoint(mousepos) or (not opp%2 and not turn%2):
                            if not board[row][column] and can:
                                if turn%2 or opp%2:
                                    board[row][column] = str(turn%2 + 1)
                                    turn += 1    
                                    allow = False
                                elif allow:
                                    while True:
                                        row = randint(0,2)
                                        column = randint(0,2)
                                        if not board[row][column]:
                                            board[row][column] = str(turn%2 + 1)
                                            turn += 1
                                            break
                    if board[row][column]:
                        available += 1
            if mouse:
                if pygame.Rect(w_canvas-100, 0, 100, 100).collidepoint(mousepos) and can:
                    break 
                if pygame.Rect(w_canvas-100, h_canvas-100, 100, 100).collidepoint(mousepos) and can:
                    opp += 1 
                if pygame.Rect(back_rect).collidepoint(mousepos):
                    game_mode = False
                    opening = True
                    break
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
            winner = check(str((turn-1)%2+1))
            allow = True
            if winner:
                scores[int(winner)-1] += 1
                break
            elif available == 9:
                break
            pygame.display.update()
            clock.tick(60)