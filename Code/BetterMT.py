import pygame
from random import randint, shuffle, choice
pygame.init()
canvas = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) 
canvas_rect = canvas.get_rect()
w_canvas = canvas_rect.right
h_canvas = canvas_rect.bottom
clock = pygame.time.Clock()
pygame.display.set_caption("Monkey Time")
hitbox = 0
cah = True
def window(background):
    global keys, mouse, mousepos, hitbox, cah
    if background: canvas.fill(background)
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()[0]
    mousepos = pygame.mouse.get_pos()
    if keys[pygame.K_ESCAPE]: pygame.quit()
    if keys[pygame.K_h]: 
        if cah: 
            hitbox += 1
            cah = False
    else: cah = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
window(False)
def draw(img, rect):
    canvas.blit(img, rect)
    if hitbox%2: pygame.draw.rect(canvas, "red", rect, width=5)
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
                    if board[row][column] == x: ac_win += 1
                    else: ac_win = 0
                    if board[column][row] == x: dw_win += 1
                    else: dw_win = 0
                    if (not row) and (not column):
                        for i in range(-1,2,2):
                            di_win = 0
                            for r in range(len(board)):
                                if board[row-r-(1*(bool(i-1)))][column-r*i] == x:
                                    di_win += 1
                            if di_win == 3:
                                return x
                    if ac_win == 3 or dw_win == 3:
                        return x
def check4(x, winc):
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
class Pipe():
    def __init__(self, h, y):
        self.rect = pygame.Rect(w_canvas, y, 75, h)
        self.cna = True
class Laser():
    def __init__(self, x, y, dir, dal):
        self.rect = pygame.Rect(x-5, y, 10, 75)
        self.dir = dir
        self.dal = dal
class Player():
    def __init__(self,rect,img):
        self.rect = rect
        self.img = pygame.image.load(img).convert_alpha()
        self.points = 0
        self.playing = 0
        self.m = 1
        self.v = 10
        self.is_jump = False
        self.cna = True
    def movement(self,moving):
        if moving[0]:
            player.is_jump = True
        if moving[1]:
            self.rect.x -= (10 + self.points*0.1)
        if moving[2]:
            self.rect.x += (10 + self.points*0.1)
back_arrow = pygame.image.load("Arrow.png").convert_alpha()
back_rect = pygame.Rect(0,0,100,100)
skins = ["Monkey", "Frog", "Dog", "Mouse", "Jedi", "Sith", "Avengers", "DC", "Brawl Stars", "HermitCraft", "Math", "Letters", "Emoji", "Soccer"]
games = ["Tic Tac Toe", "Flappy Bird", "Greedy Pig", "Knockout", "Connect 4"]
current_skin = "Monkey"
game_mode = False
startplayer = []
cards = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
suits = ["clubs","diamonds","hearts","spades"]
for i in range(8):
    startplayer.append(Player(pygame.Rect(0,0,150,150), f"MT skins/{current_skin}{i+1}.png"))
class Banana():
    def __init__(self,brandom,pos):
        self.rect = pygame.Rect(pos,0,150,150)
        if brandom == 1:
            self.value = 5
            self.img = pygame.image.load(f"MT skins/{current_skin} green.png").convert_alpha()
        elif brandom <= 3:
            self.value = -3
            self.img = pygame.image.load(f"MT skins/{current_skin} brown.png").convert_alpha()
        else:
            self.value = 1
            self.img = pygame.image.load(f"MT skins/{current_skin} yellow.png").convert_alpha()
opening = True
skin_selection = False
game_selection = False
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
                game_mode = "MT"
        if mouse:
            if skin_rect.collidepoint(mousepos):
                skin_selection = True
                page_scroll = 0
            if game_rect.collidepoint(mousepos):
                game_selection = True
        can = False
        while skin_selection:
            window("blue")
            draw(back_arrow,back_rect)
            if mouse:
                if back_rect.collidepoint(mousepos):
                    skin_selection = False
            for skin in skins:
                skin_rect = pygame.Rect(w_canvas/5*(((skins.index(skin))%4)+1)-75,250+200*int(skins.index(skin)/4)-page_scroll,150,150)
                text(skin, skin_rect.centerx, skin_rect.y+160, 50, "white", shadow=True)
                if skin == current_skin:
                    pygame.draw.rect(canvas, "green", skin_rect)
                else:
                    pygame.draw.rect(canvas, "orange", skin_rect)
                draw(pygame.image.load(f"MT skins/{skin}1.png").convert_alpha(), skin_rect)
                if mouse:
                    if skin_rect.collidepoint(mousepos) and can:
                        current_skin = skin
                        can = False
                else:
                    can = True
            text("Skin Selection", w_canvas/2, 50, 200, "white", shadow=True)
            if page_scroll < 410+150*int(len(skins)/4)-h_canvas/5*4:
                if keys[pygame.K_DOWN]:
                    page_scroll += 10
            if page_scroll > 0:
                if keys[pygame.K_UP]:
                    page_scroll -= 10
            pygame.display.update()
            clock.tick(60)
        while game_selection:
            window("blue")
            draw(back_arrow,back_rect)
            if mouse:
                if back_rect.collidepoint(mousepos):
                    game_selection = False
            for game in games:
                game_rect = pygame.Rect(w_canvas/5*(((games.index(game))%4)+1)-75,250+200*int(games.index(game)/4),150,150)
                text(game, game_rect.centerx, game_rect.y+160, 50, "white", shadow=True)
                draw(pygame.image.load(f"MT icons/{game} icon.png").convert_alpha(), game_rect)
                if mouse:
                    if game_rect.collidepoint(mousepos) and can:
                        game_mode = game
                        game_selection = False
                        opening = False
                else: can = True
            text("Game Selection", w_canvas/2, 50, 200, "white", shadow=True)
            pygame.display.update()
            clock.tick(60)
        pygame.display.update()
        clock.tick(60)
    can = True
    for i in startplayer:
        i.img = pygame.image.load(f"MT skins/{current_skin}{startplayer.index(i)+1}.png").convert_alpha()
    while game_mode == "MT" or game_mode == "Flappy Bird" or game_mode == "Greedy Pig" or game_mode == "Knockout":
        window("black")
        draw(back_arrow,back_rect)
        if mouse:
            if back_rect.collidepoint(mousepos):
                opening = True
                game_mode = False
        canstart = 0
        if game_mode == "MT" or game_mode == "Greedy Pig":
            text(f"Win Points: {winpoints}", w_canvas/2, 50, 200, "white")
            for i in range(1,6):
                pygame.draw.rect(canvas, "orange", (w_canvas*i/6-100,h_canvas-150,100,100))
                if i == 5:
                    if winpoints%50:
                        pygame.draw.rect(canvas, "green", (w_canvas*i/6-100,h_canvas-150,100,100))
                    canvas.blit(pygame.transform.scale(pygame.image.load("MT die/dice.png").convert_alpha(), (100, 100)), (w_canvas*i/6-100,h_canvas-150))
                    if mouse:
                        if pygame.Rect(w_canvas*i/6-100,h_canvas-150,100,100).collidepoint(mousepos) and can:
                            winpoints = randint(50,200)
                            pygame.time.delay(100)
                            can = False
                    else: can = True
                else:
                    if i*50 == winpoints:
                        pygame.draw.rect(canvas, "green", (w_canvas*i/6-100,h_canvas-150,100,100))
                    text(str(i*50), w_canvas*i/6-50, h_canvas-112.5, 50, "black")
                    if mouse:
                        if pygame.Rect(w_canvas*i/6-100,h_canvas-150,100,100).collidepoint(mousepos):
                            winpoints = i*50
            cnastart = 2
        elif game_mode == "Knockout":
            cnastart = 2
        else:
            cnastart = 1
        for i in startplayer: canstart += i.playing%2
        if canstart >= cnastart:
            draw(pygame.transform.rotate(back_arrow,180),(w_canvas-150,h_canvas-150,100,100))
            if mouse or keys[pygame.K_RETURN]:
                if pygame.Rect(w_canvas-150,h_canvas-150,100,100).collidepoint(mousepos) or keys[pygame.K_RETURN]:
                    players = []
                    for startplay in startplayer:
                        if startplay.playing%2:
                            players.append(startplay)
                    break
        for startplay in startplayer:
            startplay.rect.x = ((startplayer.index(startplay))%4+1)*w_canvas/5-50
            startplay.rect.y = (int(startplayer.index(startplay)/4))*250+200
            draw(startplay.img,startplay.rect)
            if mouse:
                if pygame.Rect(((startplayer.index(startplay))%4+1)*w_canvas/5-50,(int(startplayer.index(startplay)/4))*250+200,150,150).collidepoint(mousepos):
                    if can:
                        startplay.playing += 1
                        can = False
            else: can = True
            if startplay.playing%2:
                pygame.draw.rect(canvas, "green", (startplay.rect.x,startplay.rect.bottom,150,50))
                text("Playing", startplay.rect.centerx, startplay.rect.bottom+12.5, 50, "black")
            else:
                pygame.draw.rect(canvas, "orange", (startplay.rect.x,startplay.rect.bottom,150,50))
                text("Not Playing", startplay.rect.centerx, startplay.rect.bottom+12.5, 36, "black")
        pygame.display.update()
        clock.tick(60)
    if game_mode == "MT":
        running = True
        pausing = False
        bananas = []
        for player in players:
            player.rect.x = ((players.index(player))+1)*w_canvas/(len(players)+1)-50
            player.rect.y = h_canvas-350
            player.m = 1
            player.v = 10
            player.is_jump = False
        while running:
            window(False)
            canvas.blit(pygame.transform.scale(pygame.image.load(f"MT skins/{current_skin} sky.jpg").convert_alpha(), (w_canvas, h_canvas)), (0,0))
            canvas.blit(pygame.transform.scale(pygame.image.load(f"MT skins/{current_skin} grass.jpg").convert_alpha(), (w_canvas, 250)), (0,h_canvas-250))
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
                    winsc = True
                for banana in bananas:
                    if pygame.Rect.colliderect(player.rect, banana.rect):
                        player.points += banana.value
                        bananas.remove(banana)
                if keys[pygame.K_SPACE]: 
                    if can:
                        pausing = True
                        can = False
                else: can = True
                while pausing:
                    window(False)
                    pygame.draw.rect(canvas, "black", (w_canvas/2-300, h_canvas/2-300, 600, 600))
                    pygame.draw.rect(canvas, "white", (w_canvas/2-150, h_canvas/2-200, 100, 400))
                    pygame.draw.rect(canvas, "white", (w_canvas/2+50, h_canvas/2-200, 100, 400))
                    draw(back_arrow, back_rect)
                    if mouse:
                        if back_rect.collidepoint(mousepos):
                            opening = True
                            game_mode = False
                            pausing = False
                            running = False
                    if keys[pygame.K_SPACE]: 
                        if can:
                            pausing = False
                            can = False
                    else: can = True
                    pygame.display.update()
                    clock.tick(60)
            pygame.display.update()
            clock.tick(60)
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
            pygame.display.update()
            clock.tick(60)
    if game_mode == "Tic Tac Toe":
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
                            canvas.blit(pygame.image.load(f"MT skins/{current_skin}{board[row][column]}.png"),(w_canvas/2-h_canvas/2+row*h_canvas/3+75, column*h_canvas/3+75, h_canvas/3, h_canvas/3))
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
                    if back_rect.collidepoint(mousepos):
                        game_mode = False
                        opening = True
                        break
                    can = False
                else: can = True
                pygame.draw.rect(canvas, "green", (w_canvas-100, 0, 100, 100))
                text("#", w_canvas-50, -20, 200, "black")
                pygame.draw.rect(canvas, "red", (w_canvas-100, h_canvas-100, 100, 100))
                draw(pygame.image.load(f"{opp%2+1} player.png"), (w_canvas-100, h_canvas-100, 100, 100))
                text(str(scores[0]), 150, h_canvas/2+200, 200, "black")
                canvas.blit(pygame.image.load(f"MT skins/{current_skin}1.png"),(75, h_canvas/2,0,0))
                text(str(scores[1]), w_canvas-150, h_canvas/2+200, 200, "black")
                canvas.blit(pygame.image.load(f"MT skins/{current_skin}2.png"),(w_canvas-225, h_canvas/2,0,0))
                winner = check(str((turn-1)%2+1))
                allow = True
                if winner:
                    scores[int(winner)-1] += 1
                    break
                elif available == 9:
                    break
                pygame.display.update()
                clock.tick(60)
    if game_mode == "Flappy Bird":
        pipes = []
        score = 0
        pipetimer = 0
        pausing = False
        for player in players:
            player.rect.x = w_canvas/4-50
            player.rect.y = h_canvas/2-175
            player.cna = True
            player.v = 7
        while game_mode == "Flappy Bird":
            window(False)
            canvas.blit(pygame.transform.scale(pygame.image.load(f"MT skins/{current_skin} sky.jpg").convert_alpha(), (w_canvas, h_canvas)), (0,0))
            canvas.blit(pygame.transform.scale(pygame.image.load(f"MT skins/{current_skin} grass.jpg").convert_alpha(), (w_canvas, 250)), (0,h_canvas-250))
            controls = [[keys[pygame.K_w], False, False],[keys[pygame.K_i], False, False],[keys[pygame.K_g], False, False],[keys[pygame.K_UP], False, False],[keys[pygame.K_2], False, False],[keys[pygame.K_5], False, False],[keys[pygame.K_8], False, False],[keys[pygame.K_MINUS], False, False]]
            for pipe in pipes:
                pipe.rect.x -= 5
                pygame.draw.rect(canvas, "green", pipe.rect)
                if pipe.rect.right < 0:
                    pipes.remove(pipe)
                for player in players:
                    if pipe.rect.right < player.rect.left:
                        if pipe.cna:
                            score += 0.5
                            pipe.cna = False
                    if pygame.Rect.colliderect(pipe.rect, player.rect):
                        players.remove(player)
            for player in players:
                draw(player.img, player.rect)
                if pygame.Rect.colliderect(pygame.Rect(0,h_canvas-250, w_canvas, 250), player.rect):
                    players.remove(player)
                player.rect.clamp_ip(canvas_rect)
                player.movement(controls[startplayer.index(player)])
                if controls[startplayer.index(player)][0]:
                    if player.cna:
                        player.m = 1
                        player.v = 7
                        player.cna = False
                else: 
                    player.cna = True
                F1 =(1/2)*player.m*(player.v**2)
                player.rect.y -= F1
                player.v -= 1  
                if player.v < 0:
                    player.m = -0.1
                if len(players) == 1:
                    winner = startplayer.index(player)+1
            if not len(players):
                game_card = True
                break
            text(str(int(score)), w_canvas/2, 50, 200, "black", "jungleadventurer")
            pipetimer += 1
            if pipetimer >= 100:
                r1 = randint(0, h_canvas-600)
                r2 = randint(250, 500)
                pipes.append(Pipe(r1, 0))
                pipes.append(Pipe(h_canvas-250-r1-r2, r1+r2))
                pipetimer = 0
            if keys[pygame.K_SPACE]:
                if can:
                    pausing = True
                    can = False
            else: can = True
            while pausing:
                window(False)
                if keys[pygame.K_SPACE]:
                    if can:
                        pausing = False
                        can = False
                else: can = True
                pygame.draw.rect(canvas, "black", (w_canvas/3+50,h_canvas/2-300,100,600))
                pygame.draw.rect(canvas, "black", (w_canvas/3*2-150,h_canvas/2-300,100,600))
                pygame.display.update()
                clock.tick(60)
            pygame.display.update()
            clock.tick(60)
        while game_card:
            window(False)
            pygame.draw.rect(canvas, "brown", (w_canvas/2 -300, h_canvas/2 -250, 600, 600))
            text(f"Your Score: {int(score)}", w_canvas/2, h_canvas/2 -225, 100, "black", "jungleadventurer")
            text(f"Player {winner} won", w_canvas/2, h_canvas/2 -125, 100, "black", "jungleadventurer")
            text("Play again?", w_canvas/2, h_canvas/2 -25, 100, "black", "jungleadventurer")
            play_rect = pygame.Rect(w_canvas/2 -125, h_canvas/2 +75, 250, 250)
            pygame.draw.polygon(canvas, "black",[(w_canvas/2 + 100,h_canvas/2 + 200),(w_canvas/2 - 100, h_canvas/2 +100),(w_canvas/2 - 100, h_canvas/2 + 300)])
            pygame.draw.rect(canvas, "black", play_rect, width=5)
            draw(back_arrow, back_rect)
            if mouse or keys[pygame.K_RETURN]:
                if play_rect.collidepoint(mousepos) or back_rect.collidepoint(mousepos) or keys[pygame.K_RETURN]:
                    game_card = False
            pygame.display.update()
            clock.tick(60)
    if game_mode == "Greedy Pig":
        shuffle(players)
        scores = []
        for player in players:
            scores.append(0)
        while game_mode == "Greedy Pig":
            for a_player in players:
                greed_num = randint(1,6)
                roll = 0
                a_num = 0
                while True:
                    window("white")
                    for player in players:
                        player.rect.y = ((players.index(player))+1)*h_canvas/(len(players)+1)-50
                        player.rect.x = 100
                        draw(player.img, player.rect)
                        text(str(scores[players.index(player)]), 300, ((players.index(player))+1)*h_canvas/(len(players)+1), 100, "black")
                        if player == a_player:
                            canvas.blit(pygame.transform.scale(pygame.image.load(f"MT skins/{current_skin}{startplayer.index(player)+1}.png").convert_alpha(), (400, 400)), (w_canvas-400,h_canvas/2 -150))
                    endrect = pygame.Rect(w_canvas/2+50, h_canvas-150, 300, 150)
                    pygame.draw.rect(canvas, "red", endrect)
                    text("End Turn", endrect.centerx, endrect.centery-25, 100, "black")
                    canvas.blit(pygame.transform.scale(pygame.image.load("MT die/dice.png").convert_alpha(), (150, 150)), (w_canvas/2-200,h_canvas-150))
                    draw(back_arrow, back_rect)
                    if roll:
                        draw(pygame.image.load(f"MT die/Dice{roll}.png"), pygame.Rect(w_canvas/2-112.5,h_canvas/2-112.5,225,225))
                    if mouse:
                        if endrect.collidepoint(mousepos) and can:
                            scores[players.index(a_player)] += a_num
                            can = False
                            break
                        if back_rect.collidepoint(mousepos):
                            game_mode = False 
                            opening = True
                            break
                        if pygame.Rect(w_canvas/2-200, h_canvas-150, 150, 150).collidepoint(mousepos) and can:
                            can = False
                            roll = randint(1,6)
                            if roll == greed_num:
                                break
                            else:
                                a_num += roll
                    else: can = True
                    text(f"Goal: {winpoints}", w_canvas/2, 50, 200, "black") 
                    text(f"Greed number: {greed_num}", w_canvas/2, 200, 125, "black")
                    text(str(a_num), w_canvas-200, 200, 125, "black")
                    pygame.display.update()
                    clock.tick(60)
            if max(scores) >= winpoints:
                while True:
                    window(False)
                    canvas.blit(pygame.transform.scale(pygame.image.load(f"MT skins/{current_skin} sky.jpg").convert_alpha(), (w_canvas*2/3, h_canvas*2/3)), (w_canvas/6,h_canvas/6))
                    canvas.blit(pygame.transform.scale(pygame.image.load(f"MT skins/{current_skin} grass.jpg").convert_alpha(), (w_canvas*2/3, 250*2/3)), (w_canvas/6,(h_canvas)*2/3))
                    text("Winner:", w_canvas/2, 40, 200, "black") 
                    text("Play again?", w_canvas/2, 160, 100, "black") 
                    draw(back_arrow, back_rect)
                    canvas.blit(pygame.transform.scale(pygame.image.load(f"MT skins/{current_skin}{startplayer.index(players[scores.index(max(scores))])+1}.png").convert_alpha(), (400, 400)), (w_canvas/2-200,h_canvas/2-200))
                    if mouse:
                        if pygame.Rect(w_canvas/2-200,h_canvas/2-200,400,400).collidepoint(mousepos):
                            shuffle(players)
                            scores = []
                            for player in players:
                                scores.append(0)
                            break
                        if back_rect.collidepoint(mousepos):
                            game_mode = False 
                            opening = True
                            break
                    pygame.display.update()
                    clock.tick(60)
    if game_mode == "Knockout":
        pausing = False
        game_card = False
        teams = players.copy()
        shuffle(teams)
        team_1 = []
        team_2 = []
        lasers = []
        turn = 0
        for player in range(len(teams)):
            opp = randint(0,len(teams)-1)
            if turn%2:
                team_1.append(teams[opp])
            else:
                team_2.append(teams[opp])
            turn += 1
            teams.remove(teams[opp])
        for player in team_1:
            player.rect.x = ((team_1.index(player))+1)*w_canvas/(len(team_1)+1)-50
            player.rect.y = 0
            player.v = 0
            player.m = 3
        for player in team_2:
            player.rect.x = ((team_2.index(player))+1)*w_canvas/(len(team_2)+1)-50
            player.rect.y = h_canvas-150
            player.v = 0
            player.m = 3
        while game_mode == "Knockout":
            window("darkgreen")
            pygame.draw.rect(canvas, "black", (0,150,w_canvas,h_canvas-300))
            controls = [[keys[pygame.K_w], keys[pygame.K_a], keys[pygame.K_d]],[keys[pygame.K_i], keys[pygame.K_j], keys[pygame.K_l]],[keys[pygame.K_g], keys[pygame.K_v], keys[pygame.K_b]],[keys[pygame.K_UP], keys[pygame.K_LEFT], keys[pygame.K_RIGHT]],[keys[pygame.K_2], keys[pygame.K_1], keys[pygame.K_3]],[keys[pygame.K_5], keys[pygame.K_4], keys[pygame.K_6]],[keys[pygame.K_8], keys[pygame.K_7], keys[pygame.K_9]],[keys[pygame.K_MINUS], keys[pygame.K_0], keys[pygame.K_EQUALS]]]
            for player in players:
                player.movement(controls[startplayer.index(player)])
                player.v += 1
                if player.m <= 0:
                    players.remove(player)
                for laser in lasers:
                    if pygame.Rect.colliderect(laser.rect, player.rect):
                        lasers.remove(laser)
                        player.m -= 1
                if player.rect.centerx < 0:
                    player.rect.x = w_canvas - 75
                elif player.rect.centerx > w_canvas:
                    player.rect.x = -75
                draw(player.img, player.rect)
            for player in team_1:
                if player.is_jump and player.v > 60:
                    lasers.append(Laser(player.rect.centerx, player.rect.bottom, 1, w_canvas))
                    player.v = 0
                else:
                    player.is_jump = False
                if player.m <= 0:
                    team_1.remove(player)
                pygame.draw.rect(canvas, "red", (player.rect.x, player.rect.bottom, 150*player.m/3,20))
                pygame.draw.rect(canvas, "white", (player.rect.x, player.rect.bottom, 150,20), width=5)
            for player in team_2:
                if player.is_jump and player.v > 60:
                    lasers.append(Laser(player.rect.centerx, player.rect.y-75, -1, w_canvas))
                    player.v = 0
                else:
                    player.is_jump = False
                if player.m <= 0:
                    team_2.remove(player)
                pygame.draw.rect(canvas, "red", (player.rect.x, player.rect.y-20, 150*player.m/3,20))
                pygame.draw.rect(canvas, "white", (player.rect.x, player.rect.y-20, 150,20), width=5)
            if not len(team_1):
                game_card = True
                winner = 1
                break
            elif not len(team_2):
                game_card = True
                winner = 2
                break
            for laser in lasers:
                laser.rect.y += 20*laser.dir
                pygame.draw.rect(canvas, "red", laser.rect)
                if not -100 < laser.rect.y < w_canvas:
                    lasers.remove(laser)
            if keys[pygame.K_SPACE]: 
                if can:
                    pausing = True
                    can = False
            else: can = True
            while pausing:
                window(False)
                pygame.draw.rect(canvas, "black", (w_canvas/2-300, h_canvas/2-300, 600, 600))
                pygame.draw.rect(canvas, "white", (w_canvas/2-150, h_canvas/2-200, 100, 400))
                pygame.draw.rect(canvas, "white", (w_canvas/2+50, h_canvas/2-200, 100, 400))
                draw(back_arrow, back_rect)
                if mouse:
                    if back_rect.collidepoint(mousepos):
                        opening = True
                        game_mode = False
                        pausing = False
                if keys[pygame.K_SPACE]: 
                    if can:
                        pausing = False
                        can = False
                else: can = True
                pygame.display.update()
                clock.tick(60)
            pygame.display.update()
            clock.tick(60)
        while game_card:
            window(False)
            pygame.draw.rect(canvas, "brown", (w_canvas/2 -300, h_canvas/2 -250, 600, 600))
            text(f"Winner:", w_canvas/2, h_canvas/2 -225, 100, "black", "jungleadventurer")
            text(f"Team {winner}", w_canvas/2, h_canvas/2 -125, 100, "black", "jungleadventurer")
            text("Play again?", w_canvas/2, h_canvas/2 -25, 100, "black", "jungleadventurer")
            play_rect = pygame.Rect(w_canvas/2 -125, h_canvas/2 +75, 250, 250)
            pygame.draw.polygon(canvas, "black",[(w_canvas/2 + 100,h_canvas/2 + 200),(w_canvas/2 - 100, h_canvas/2 +100),(w_canvas/2 - 100, h_canvas/2 + 300)])
            pygame.draw.rect(canvas, "black", play_rect, width=5)
            draw(back_arrow, back_rect)
            if mouse or keys[pygame.K_RETURN]:
                if play_rect.collidepoint(mousepos) or back_rect.collidepoint(mousepos) or keys[pygame.K_RETURN]:
                    game_card = False
            pygame.display.update()
            clock.tick(60)
    if game_mode == "Connect 4":
        opp = 1
        scores = [0,0]
        while game_mode == "Connect 4":
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
                            canvas.blit(pygame.transform.scale(pygame.image.load(f"MT skins/{current_skin}{board[row][column]}.png").convert_alpha(), (h_canvas/7, h_canvas/7)), (w_canvas/2-h_canvas/2+row*h_canvas/7, column*h_canvas/7))
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
                draw(back_arrow, back_rect)
                if mouse:
                    if back_rect.collidepoint(mousepos):
                        opening = True
                        game_mode = False
                        break
                text(f"{opp%2+1}", w_canvas-50, h_canvas-100, 200, "black")
                text(str(scores[0]), 150, h_canvas/2+200, 200, "black")
                canvas.blit(pygame.image.load(f"MT skins/{current_skin}1.png"),(75, h_canvas/2,0,0))
                text(str(scores[1]), w_canvas-150, h_canvas/2+200, 200, "black")
                canvas.blit(pygame.image.load(f"MT skins/{current_skin}2.png"),(w_canvas-225, h_canvas/2,0,0))
                winner = check4(str((turn-1)%2+1), 4)
                allow = True
                if winner:
                    scores[int(winner)-1] += 1
                    break
                elif available == 49:
                    break
                pygame.display.update()
                clock.tick(60)