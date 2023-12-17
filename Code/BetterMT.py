import pygame
from random import randint
pygame.init()
canvas = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) 
canvas_rect = canvas.get_rect()
w_canvas = canvas_rect.right
h_canvas = canvas_rect.bottom
clock = pygame.time.Clock()
pygame.display.set_caption("Monkey Time")
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
window(False)
def text(text, x, y, si, col, font="jungle adventurer"):
    font = pygame.font.SysFont(font,si)
    texting = font.render(text, True, col)
    x -= texting.get_width()/2
    canvas.blit(texting, (x,y))
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
skins = ["Monkey", "Frog", "Jedi", "Sith"]
current_skin = "Monkey"
startplayer = []
for i in range(4):
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
skinui = False
running = False
winsc = False
winpoints = 100
while True:
    while opening:
        window("blue")
        text("Monkey Time", w_canvas/2+10, 50+10, 300, "black")
        text("Monkey Time", w_canvas/2, 50, 300, "white")
        text("(But Better)", w_canvas-200, 250, 50, "black")
        play_rect = pygame.Rect(w_canvas/2 -125, h_canvas/2 - 125, 250, 250)
        pygame.draw.rect(canvas, "green", play_rect)
        pygame.draw.polygon(canvas, "black",[(w_canvas/2 + 100,h_canvas/2),(w_canvas/2 - 100, h_canvas/2 - 100),(w_canvas/2 - 100, h_canvas/2 + 100)])
        pygame.draw.rect(canvas, "black", play_rect, width=5)
        skin_rect = pygame.Rect(w_canvas-300, h_canvas-300, 150, 150)
        canvas.blit(pygame.image.load("skin.png").convert_alpha(), skin_rect)
        if mouse or keys[pygame.K_RETURN]:
            if play_rect.collidepoint(mousepos) or keys[pygame.K_RETURN]:
                opening = False
                openui = True
            if skin_rect.collidepoint(mousepos):
                skinui = True
        while skinui:
            window("blue")
            canvas.blit(back_arrow,(0,0,100,100))
            if mouse:
                if pygame.Rect((0,0,100,100)).collidepoint(mousepos):
                    skinui = False
            for skin in skins:
                skin_rect = pygame.Rect(w_canvas/5*(((skins.index(skin))%4)+1)-75,250+150*int(skins.index(skin)/4),150,150)
                if skin == current_skin:
                    pygame.draw.rect(canvas, "green", skin_rect)
                else:
                    pygame.draw.rect(canvas, "orange", skin_rect)
                canvas.blit(pygame.image.load(f"{skin}1.png").convert_alpha(), skin_rect)
                if mouse:
                    if skin_rect.collidepoint(mousepos):
                        current_skin = skin
            pygame.display.update()
            clock.tick(60)
        pygame.display.update()
        clock.tick(60)
    can = True
    for i in startplayer:
        i.img = pygame.image.load(f"{current_skin}{startplayer.index(i)+1}.png").convert_alpha()
    while openui:
        window("black")
        text(f"Win Points: {winpoints}", w_canvas/2, 50, 200, "white")
        canvas.blit(back_arrow,(0,0,100,100))
        if mouse:
                if pygame.Rect((0,0,100,100)).collidepoint(mousepos):
                    openui = False
                    opening = True
        for i in range(1,6):
            pygame.draw.rect(canvas, "orange", (w_canvas*i/6-100,h_canvas-150,100,100))
            if i == 5:
                if winpoints%50:
                    pygame.draw.rect(canvas, "green", (w_canvas*i/6-100,h_canvas-150,100,100))
                text("RND", w_canvas*i/6-50, h_canvas-112.5, 50, "black")
                if mouse:
                    if pygame.Rect(w_canvas*i/6-100,h_canvas-150,100,100).collidepoint(mousepos):
                        winpoints = randint(50,200)
                        pygame.time.delay(100)
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
            canvas.blit(pygame.transform.rotate(back_arrow,180),(w_canvas-150,h_canvas-150,100,100))
            if mouse or keys[pygame.K_RETURN]:
                if pygame.Rect(w_canvas-150,h_canvas-150,100,100).collidepoint(mousepos) or keys[pygame.K_RETURN]:
                    openui = False
        for startplay in startplayer:
            startplay.rect.x = ((startplayer.index(startplay))%4+1)*w_canvas/5-50
            startplay.rect.y = (int(startplayer.index(startplay)/4)+1)*h_canvas/int(len(startplayer)/2+2)+50
            canvas.blit(startplay.img,startplay.rect)
            if mouse:
                if pygame.Rect(((startplayer.index(startplay))%4+1)*w_canvas/5-50,(int(startplayer.index(startplay)/4)+1)*h_canvas/int(len(startplayer)/2+2)+50,150,150).collidepoint(mousepos):
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
    if not opening:
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
        canvas.blit(pygame.transform.scale(pygame.image.load("sky1.jpg").convert(), (w_canvas, h_canvas)), (0,0))
        canvas.blit(pygame.transform.scale(pygame.image.load("grass1.jpg").convert(), (w_canvas, h_canvas/4)), (0,h_canvas-h_canvas/4))
        pygame.draw.rect(canvas, "black", (0,0,w_canvas,150))
        text(f"Goal: {winpoints}", 750, 50, 100, "white")
        if len(bananas) < 5:
            bananas.append(Banana(randint(1,10),randint(0,w_canvas-150)))
        for banana in bananas:
            canvas.blit(banana.img,banana.rect)
            banana.rect.y += 10
            if banana.rect.y >= h_canvas:
                bananas.remove(banana)
        controls = [[keys[pygame.K_w], keys[pygame.K_a], keys[pygame.K_d]],[keys[pygame.K_i], keys[pygame.K_j], keys[pygame.K_l]],[keys[pygame.K_g], keys[pygame.K_v], keys[pygame.K_b]],[keys[pygame.K_UP], keys[pygame.K_LEFT], keys[pygame.K_RIGHT]]]
        for player in players:
            canvas.blit(player.img,player.rect)
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
    if not opening:
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
            canvas.blit(banana.img,banana.rect)
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
                openui = True
        pygame.display.update()
        clock.tick(60)