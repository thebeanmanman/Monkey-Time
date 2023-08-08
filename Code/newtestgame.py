import pygame
from random import randint
pygame.init()
master = True
page = True
exit = True
Open_ui = True
Tic_Tac_Toe = False
canvas = pygame.display.set_mode((1500, 1000))
canvas_rect = canvas.get_rect()
clock = pygame.time.Clock()


lightblue = ("#00b2ff")
blue = (0,0,255)
white = (255,255,255)
green= (45, 175, 0)
yellow= (254, 237, 90)
black = (0,0,0)
light_green = (20, 225, 0)
orange = (255,140,0)
purple = (153,50,204)
pink = (255,0,255)
red = "red"
deck = 553

skyrect = pygame.Rect(0,0, 1500, 1000)
grassrect = pygame.Rect(0,700, 1500, 300)
winner = ""
keys = pygame.key.get_pressed()

    

class juump(object):
    def __init__(self, m, v, is_jump):
        self.m = m
        self.v = v
        self.is_jump = is_jump
p1points = 0
p2points = 0
p3points = 0
p4points = 0
winpoints = 0

def text(text, a, b, si, col):
    font= pygame.font.SysFont("arial",si)
    texting = font.render(text, True, col)
    canvas.blit(texting, (a,b))


pj1 = juump(1, 10, False)
pj2 = juump(1, 10, False)
pj3 = juump(1, 10, False)
pj4 = juump(1, 10, False)

startrect = pygame.Rect(1200,800,200,100)
exitrect = pygame.Rect(200,750,150,150)
menurect = pygame.Rect(675,750,150,150)
playagainrect = pygame.Rect(1150,750,150,150)
playrect = pygame.Rect(600,350,300,300)
settingsrect = pygame.Rect(100,750,150,150)
skinrect = pygame.Rect(1250,750,150,150)
pointselect50 = pygame.Rect(200,800,100,100)
pointselect100 = pygame.Rect(400,800,100,100)
pointselect150 = pygame.Rect(600,800,100,100)
pointselect200 = pygame.Rect(800,800,100,100)
       
player1 = pygame.Rect(125, deck, 150, 147)
player2 = pygame.Rect(500, deck, 150, 147)
player3 = pygame.Rect(875, deck, 150, 147)
player4 = pygame.Rect(1250, deck, 150, 147)
start_player1 = pygame.Rect(200, 200, 150, 147)
start_player2 = pygame.Rect(1050, 200, 150, 147)
start_player3 = pygame.Rect(200, 500, 150, 147)
start_player4 = pygame.Rect(1050, 500, 150, 147)
primary = True


try:
    sky = pygame.image.load("sky1.jpg")
    sky = pygame.transform.scale(sky, (1500, 1200))
    grass = pygame.image.load("grass1.jpg")
    grass = pygame.transform.scale(grass, (1500, 300))
    start = pygame.image.load("start.png")
    exiticon = pygame.image.load("exiticon.png")
    menu = pygame.image.load("menu.png")
    playagain = pygame.image.load("playagain.png")
    playbutton = pygame.image.load("playbutton.png")
    player1img = pygame.image.load("monkeman21.png")
    player2img = pygame.image.load("monkeman1.png")
    player3img = pygame.image.load("monkey3.png")
    player4img = pygame.image.load("monkey4.png")
    startplayer1img = pygame.image.load("monkeman21.png")
    startplayer2img = pygame.image.load("monkeman1.png")
    startplayer3img = pygame.image.load("monkey3.png")
    startplayer4img = pygame.image.load("monkey4.png")
    yellowe = pygame.image.load("banan.png")
    yellowe = pygame.transform.scale(yellowe, (180,180))
    blacke = pygame.image.load("brownbanan.png")
    blacke = pygame.transform.scale(blacke, (180,180))
    bluee = pygame.image.load("greenbanan.png")
    bluee = pygame.transform.scale(bluee, (180,180))
    skin = pygame.image.load("skin.png")
    settings = pygame.image.load("settings.png")
    def draw(img, pos):
        return canvas.blit(img, pos)
except FileNotFoundError:
    #[colour, rect]
    sky = lightblue
    grass = green
    start = green
    exiticon = red
    menu = blue
    playbutton = green
    playagain = green
    player1img = purple
    player2img = orange
    player3img = pink
    player4img = red
    startplayer1img = purple
    startplayer2img = orange
    startplayer3img = pink
    startplayer4img = red
    yellowe = yellow
    blacke = black
    bluee = light_green
    skin = yellow
    settings = "grey"
    primary = False
    def draw(img, rect):
        return pygame.draw.rect(canvas, img, rect)

class Player(object):
    def __init__(self, jump, left, right):
        self.jump = jump
        self.left = left
        self.right = right

class banana(object):
    def __init__(self, picture, initfallspeed, worth):
        self.picture = picture
        self.initfallspeed = initfallspeed
        self.worth = worth
    def addfall(self):
        self.initfallspeed += 0.25
   
def bananana(initx):
    return pygame.Rect(initx, 0, 150, 147)


def Random_b():
    randomc = randint(1, 10)
    if randomc == 1:
        randomco = bluee
        randomnu = 5
    elif randomc <= 3:
        randomco = blacke
        randomnu = -1
    else:
        randomco = yellowe
        randomnu = 1
    return [randomco, randomnu]
def Randompos():
    randomp = randint(0, 1350)
    return randomp


random_b = Random_b()
randompos = Randompos()
       
banana1 = banana(random_b[0], 2, random_b[1])
random_b = Random_b()
banana2 = banana(random_b[0], 2, random_b[1])
random_b = Random_b()
banana3 = banana(random_b[0], 2, random_b[1])
random_b = Random_b()
banana4 = banana(random_b[0], 2, random_b[1])
random_b = Random_b()
banana5 = banana(random_b[0], 2, random_b[1])
random_b = Random_b()


Banana_rect1 = bananana(randompos)
randompos = Randompos()
Banana_rect2 = bananana(randompos)
randompos = Randompos()
Banana_rect3 = bananana(randompos)
randompos = Randompos()
Banana_rect4 = bananana(randompos)
randompos = Randompos()
Banana_rect5 = bananana(randompos)

def resetorangei():
    global orangei1
    global orangei2
    global orangei3
    global orangei4
    orangei1 = orange
    orangei2 = orange
    orangei3 = orange
    orangei4 = orange


isplay1 = 0
isplay2 = 0
isplay3 = 0
isplay4 = 0
can_start = 2
pygame.display.set_caption("Monkey Time 2.0")

while master:
    while page:
        canvas.fill(lightblue)
        draw(playbutton, playrect)
        if primary:
            draw(skin, skinrect)
        #draw(settings, settingsrect)
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()[0]
        mousepos = pygame.mouse.get_pos()
        if mouse:
            if playrect.collidepoint(mousepos):
                    Open_ui = False
                    page = False
        if keys[pygame.K_q] and keys[pygame.K_p]:
            pygame.quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update() 
    while not Open_ui:
        canvas.fill(black)
        can_start = isplay1%2 + isplay2%2 + isplay3%2 + isplay4%2
        mouse = pygame.mouse.get_pressed()[0]
        mousepos = pygame.mouse.get_pos()
        if can_start >= 2 and winpoints > 0:
            draw(start, startrect)
            if mouse:
                if startrect.collidepoint(mousepos):
                    exit = False
                    Open_ui = True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                exit = False
                Open_ui = True
        keys = pygame.key.get_pressed()
        draw(startplayer1img, start_player1)
        draw(startplayer2img, start_player2)
        draw(startplayer3img, start_player3)
        draw(startplayer4img, start_player4)
        if winpoints == 50:
            resetorangei()
            orangei1 = green
        elif winpoints == 100:
            resetorangei()
            orangei2 = green
        elif winpoints == 150:
            resetorangei()
            orangei3 = green
        elif winpoints == 200:
            resetorangei()
            orangei4 = green
        else:
            resetorangei()
        pygame.draw.rect(canvas, orangei1, pointselect50)
        pygame.draw.rect(canvas, orangei2, pointselect100)
        pygame.draw.rect(canvas, orangei3, pointselect150)
        pygame.draw.rect(canvas, orangei4, pointselect200)
        text("50", 225, 825, 50, black)
        text("100", 412.5, 825, 50, black)
        text("150", 612.5, 825, 50, black)
        text("200", 812.5, 825, 50, black)
        if mouse:
            if start_player1.collidepoint(mousepos):
                isplay1 += 1
                pygame.time.delay(100)
            if start_player2.collidepoint(mousepos):
                isplay2 += 1
                pygame.time.delay(100)
            if start_player3.collidepoint(mousepos):
                isplay3 += 1
                pygame.time.delay(100)
            if start_player4.collidepoint(mousepos):
                isplay4 += 1
                pygame.time.delay(100)
            if  pointselect50.collidepoint(mousepos):
                winpoints = 50
                pygame.time.delay(100)
            if pointselect100.collidepoint(mousepos):
                winpoints = 100
                pygame.time.delay(100)
            if pointselect150.collidepoint(mousepos):
                winpoints = 150
                pygame.time.delay(100)
            if pointselect200.collidepoint(mousepos):
                winpoints = 200
                pygame.time.delay(100)
        if keys[pygame.K_0]:
            isplay1 += 1
            isplay2 += 1
            isplay3 += 1
            isplay4 += 1
            pygame.time.delay(200)
        if keys[pygame.K_1]:
            isplay1 += 1
            pygame.time.delay(200)
        if keys[pygame.K_2]:
            isplay2 += 1
            pygame.time.delay(200)
        if keys[pygame.K_3]:
            isplay3 += 1
            pygame.time.delay(200)
        if keys[pygame.K_4]:
            isplay4 += 1
            pygame.time.delay(200)
        if isplay1%2:
            text("Player 1 is playing",200,350,50,green)
        else:
            text("Player 1 is not playing",200,350,50,red)
        if isplay2%2:
            text("Player 2 is playing",1050,350,50,green)
        else:
            text("Player 2 is not playing",1050,350,50,red)
        if isplay3%2:
            text("Player 3 is playing",200,650,50,green)
        else:
            text("Player 3 is not playing",200,650,50,red)
        if isplay4%2:
            text("Player 4 is playing",1050,650,50,green)
        else:
            text("Player 4 is not playing",1050,650,50,red)
        if keys[pygame.K_q] and keys[pygame.K_p]:
            pygame.quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()

    while not exit:
        canvas.fill(white)
        draw(sky, skyrect)
        keys = pygame.key.get_pressed()
        if isplay1%2:
            draw(player1img, player1)
        if isplay2%2:
            draw(player2img, player2)
        if isplay3%2:
            draw(player3img, player3)
        if isplay4%2:
            draw(player4img, player4)
        draw(banana1.picture, Banana_rect1)
        draw(banana2.picture, Banana_rect2)
        draw(banana3.picture, Banana_rect3)
        draw(banana4.picture, Banana_rect4)
        draw(banana5.picture, Banana_rect5)
        if isplay1%2:
            text(str(p1points),100,20,150,white)
        if isplay2%2:
            text(str(p2points),1300,20,150,white)
        if isplay3%2:
            text(str(p3points),100,170,150,white)
        if isplay4%2:
            text(str(p4points),1300,170,150,white)

        Banana_rect1.y += banana1.initfallspeed
        Banana_rect2.y += banana2.initfallspeed
        Banana_rect3.y += banana3.initfallspeed
        Banana_rect4.y += banana4.initfallspeed
        Banana_rect5.y += banana5.initfallspeed
       
        if Banana_rect1.top > deck:
            Banana_rect1.y = 0
            Banana_rect1.x = Randompos()
            random_b = Random_b()
            banana1 = banana(random_b[0], 2, random_b[1])
        if Banana_rect2.top > deck:
            Banana_rect2.y = 0
            Banana_rect2.x = Randompos()
            random_b = Random_b()
            banana2 = banana(random_b[0], 2, random_b[1])
        if Banana_rect3.top > deck:
            Banana_rect3.y = 0
            Banana_rect3.x = Randompos()
            random_b = Random_b()
            banana3 = banana(random_b[0], 2, random_b[1])
        if Banana_rect4.top > deck:
            Banana_rect4.y = 0
            Banana_rect4.x = Randompos()
            random_b = Random_b()
            banana4 = banana(random_b[0], 2, random_b[1])
        if Banana_rect5.top > deck:
            Banana_rect5.y = 0
            Banana_rect5.x = Randompos()
            random_b = Random_b()
            banana5 = banana(random_b[0], 2, random_b[1])


       
        p1 = Player(keys[pygame.K_w], keys[pygame.K_a], keys[pygame.K_d])
        p2 = Player(keys[pygame.K_i], keys[pygame.K_j], keys[pygame.K_l])
        p3 = Player(keys[pygame.K_UP], keys[pygame.K_LEFT], keys[pygame.K_RIGHT])
        p4 = Player(keys[pygame.K_g], keys[pygame.K_v], keys[pygame.K_b])


        if player1.y > deck:
            player1.y=deck
        if player2.y > deck:
            player2.y=deck
        if player3.y > deck:
            player3.y=deck
        if player4.y > deck:
            player4.y=deck
        if p1.right:
            player1.move_ip((7.5 + 0.1*p1points), 0)    
        if p1.left:
            player1.move_ip(-(7.5 + 0.1*p1points), 0)
        if p1.jump:
            pj1.is_jump = True
        if p2.right:
            player2.move_ip((7.5 + 0.1*p2points), 0)    
        if p2.left:
            player2.move_ip(-(7.5 + 0.1*p2points), 0)
        if p2.jump:
            pj2.is_jump = True
        if p3.right:
            player3.move_ip((7.5 + 0.1*p3points), 0)    
        if p3.left:
            player3.move_ip(-(7.5 + 0.1*p3points), 0)
        if p3.jump:
            pj3.is_jump = True
        if p4.right:
            player4.move_ip((7.5 + 0.1*p3points), 0)    
        if p4.left:
            player4.move_ip(-(7.5 + 0.1*p3points), 0)
        if p4.jump:
            pj4.is_jump = True
        if pj1.is_jump:
            F1 =(1 / 2)*pj1.m*(pj1.v**2)
            player1.y -= F1
            pj1.v -= 1
            if pj1.v<0:
                pj1.m =-1
            if pj1.v ==-11:
                pj1.is_jump = False
                pj1.v = 10
                pj1.m = 1
        pygame.time.delay(10)
        if pj2.is_jump:
            F2 =(1 / 2)*pj2.m*(pj2.v**2)
            player2.y -= F2
            pj2.v -= 1
            if pj2.v<0:
                pj2.m =-1
            if pj2.v ==-11:
                pj2.is_jump = False
                pj2.v = 10
                pj2.m = 1
        if pj3.is_jump:
            F3 =(1 / 2)*pj3.m*(pj3.v**2)
            player3.y -= F3
            pj3.v -= 1
            if pj3.v<0:
                pj3.m =-1
            if pj3.v ==-11:
                pj3.is_jump = False
                pj3.v = 10
                pj3.m = 1      
        if pj4.is_jump:
            F4 =(1 / 2)*pj4.m*(pj4.v**2)
            player4.y -= F4
            pj4.v -= 1
            if pj4.v<0:
                pj4.m =-1
            if pj4.v ==-11:
                pj4.is_jump = False
                pj4.v = 10
                pj4.m = 1  
        if isplay1%2:        
            if pygame.Rect.colliderect(player1, Banana_rect1) == True:
                p1points += banana1.worth
                Banana_rect1.y = 0
                banana1.addfall()
                Banana_rect1.x = Randompos()
                random_b = Random_b()
                banana1 = banana(random_b[0], 2, random_b[1])
            if pygame.Rect.colliderect(player1, Banana_rect2) == True:
                p1points += banana2.worth
                Banana_rect2.y = 0
                banana2.addfall()
                Banana_rect2.x = Randompos()
                random_b = Random_b()
                banana2 = banana(random_b[0], 2, random_b[1])
            if pygame.Rect.colliderect(player1, Banana_rect3) == True:
                p1points += banana3.worth
                Banana_rect3.y = 0
                banana3.addfall()
                Banana_rect3.x = Randompos()
                random_b = Random_b()
                banana3 = banana(random_b[0], 2, random_b[1])
            if pygame.Rect.colliderect(player1, Banana_rect4) == True:
                p1points += banana4.worth
                Banana_rect4.y = 0
                banana4.addfall()
                Banana_rect4.x = Randompos()
                random_b = Random_b()
                banana4 = banana(random_b[0], 2, random_b[1])
            if pygame.Rect.colliderect(player1, Banana_rect5) == True:
                p1points += banana5.worth
                Banana_rect5.y = 0
                banana5.addfall()
                Banana_rect5.x = Randompos()
                random_b = Random_b()
                banana5 = banana(random_b[0], 2, random_b[1])
        if isplay2%2:
            if pygame.Rect.colliderect(player2, Banana_rect1) == True:
                p2points += banana1.worth
                Banana_rect1.y = 0
                banana1.addfall()
                Banana_rect1.x = Randompos()
                random_b = Random_b()
                banana1 = banana(random_b[0], 2, random_b[1])
            if pygame.Rect.colliderect(player2, Banana_rect2) == True:
                p2points += banana2.worth
                Banana_rect2.y = 0
                banana2.addfall()
                Banana_rect2.x = Randompos()
                random_b = Random_b()
                banana2 = banana(random_b[0], 2, random_b[1])
            if pygame.Rect.colliderect(player2, Banana_rect3) == True:
                p2points += banana3.worth
                Banana_rect3.y = 0
                banana3.addfall()
                Banana_rect3.x = Randompos()
                random_b = Random_b()
                banana3 = banana(random_b[0], 2, random_b[1])
            if pygame.Rect.colliderect(player2, Banana_rect4) == True:
                p2points += banana4.worth
                Banana_rect4.y = 0
                banana4.addfall()
                Banana_rect4.x = Randompos()
                random_b = Random_b()
                banana4 = banana(random_b[0], 2, random_b[1])
            if pygame.Rect.colliderect(player2, Banana_rect5) == True:
                p2points += banana5.worth
                Banana_rect5.y = 0
                banana5.addfall()
                Banana_rect5.x = Randompos()
                random_b = Random_b()
                banana5 = banana(random_b[0], 2, random_b[1])
        if isplay3%2:
            if pygame.Rect.colliderect(player3, Banana_rect1) == True:
                p3points += banana1.worth
                Banana_rect1.y = 0
                banana1.addfall()
                Banana_rect1.x = Randompos()
                random_b = Random_b()
                banana1 = banana(random_b[0], 2, random_b[1])
            if pygame.Rect.colliderect(player3, Banana_rect2) == True:
                p3points += banana2.worth
                Banana_rect2.y = 0
                banana2.addfall()
                Banana_rect2.x = Randompos()
                random_b = Random_b()
                banana2 = banana(random_b[0], 2, random_b[1])
            if pygame.Rect.colliderect(player3, Banana_rect3) == True:
                p3points += banana3.worth
                Banana_rect3.y = 0
                banana3.addfall()
                Banana_rect3.x = Randompos()
                random_b = Random_b()
                banana3 = banana(random_b[0], 2, random_b[1])
            if pygame.Rect.colliderect(player3, Banana_rect4) == True:
                p3points += banana4.worth
                Banana_rect4.y = 0
                banana4.addfall()
                Banana_rect4.x = Randompos()
                random_b = Random_b()
                banana4 = banana(random_b[0], 2, random_b[1])
            if pygame.Rect.colliderect(player3, Banana_rect5) == True:
                p3points += banana5.worth
                Banana_rect5.y = 0
                banana5.addfall()
                Banana_rect5.x = Randompos()
                random_b = Random_b()
                banana5 = banana(random_b[0], 2, random_b[1])
        if isplay4%2:
            if pygame.Rect.colliderect(player4, Banana_rect1) == True:
                p4points += banana1.worth
                Banana_rect1.y = 0
                banana1.addfall()
                Banana_rect1.x = Randompos()
                random_b = Random_b()
                banana1 = banana(random_b[0], 2, random_b[1])
            if pygame.Rect.colliderect(player4, Banana_rect2) == True:
                p4points += banana2.worth
                Banana_rect2.y = 0
                banana2.addfall()
                Banana_rect2.x = Randompos()
                random_b = Random_b()
                banana2 = banana(random_b[0], 2, random_b[1])
            if pygame.Rect.colliderect(player4, Banana_rect3) == True:
                p4points += banana3.worth
                Banana_rect3.y = 0
                banana3.addfall()
                Banana_rect3.x = Randompos()
                random_b = Random_b()
                banana3 = banana(random_b[0], 2, random_b[1])
            if pygame.Rect.colliderect(player4, Banana_rect4) == True:
                p4points += banana4.worth
                Banana_rect4.y = 0
                banana4.addfall()
                Banana_rect4.x = Randompos()
                random_b = Random_b()
                banana4 = banana(random_b[0], 2, random_b[1])
            if pygame.Rect.colliderect(player4, Banana_rect5) == True:
                p4points += banana5.worth
                Banana_rect5.y = 0
                banana5.addfall()
                Banana_rect5.x = Randompos()
                random_b = Random_b()
                banana5 = banana(random_b[0], 2, random_b[1])
        if p1points >= winpoints:
            winner = "Player 1"
            exit = True
            winning = True
        if p2points >= winpoints:
            winner = "Player 2"
            exit = True
            winning = True
        if p3points >= winpoints:
            winner = "Player 3"
            exit = True
            winning = True
        if p4points >= winpoints:
            winner = "Player 4"
            exit = True
            winning = True
        draw(grass, grassrect)
        if keys[pygame.K_q] and keys[pygame.K_p]:
            pygame.quit()
        player1.clamp_ip(canvas_rect)
        player2.clamp_ip(canvas_rect)
        player3.clamp_ip(canvas_rect)
        player4.clamp_ip(canvas_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
        clock.tick(600)

    while winning:
        canvas.fill(yellow)
        text(f"{winner} is Full",200,300,200,black)
        draw(exiticon, exitrect)
        draw(menu, menurect)
        draw(playagain, playagainrect)
        p1points = 0
        p2points = 0
        p3points = 0
        p4points = 0
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()[0]
        mousepos = pygame.mouse.get_pos()
        if mouse:
            if exitrect.collidepoint(mousepos):
                pygame.quit()
            if menurect.collidepoint(mousepos):
                winning = False
                page = True
                isplay1 = 0
                isplay2 = 0
                isplay3 = 0
                isplay4 = 0
                player1 = pygame.Rect(100, deck, 150, 147)
                player2 = pygame.Rect(900, deck, 150, 147)
                player3 = pygame.Rect(700, deck, 150, 147)
                player4 = pygame.Rect(300, deck, 150, 147)
                Banana_rect1.y = 0
                Banana_rect2.y = 0
                Banana_rect3.y = 0
                Banana_rect4.y = 0
                Banana_rect5.y = 0
            if playagainrect.collidepoint(mousepos):
                winning = False
                exit = False
                player1 = pygame.Rect(100, deck, 150, 147)
                player2 = pygame.Rect(900, deck, 150, 147)
                player3 = pygame.Rect(700, deck, 150, 147)
                player4 = pygame.Rect(300, deck, 150, 147)
                Banana_rect1.y = 0
                Banana_rect2.y = 0
                Banana_rect3.y = 0
                Banana_rect4.y = 0
                Banana_rect5.y = 0
        for event in pygame.event.get():
	        if event.type == pygame.QUIT:
                    pygame.quit()
        if keys[pygame.K_q] and keys[pygame.K_p]:
            pygame.quit()
        pygame.display.update()
        clock.tick(600)

    while Tic_Tac_Toe:
        board = [[" "," ", " "],[" ", " ", " "],[" "," "," "]]
        T_win = False
        def display_board():
            print(" |1|2|3|")
            for colum in range(len(board)):
                rowe = f"{colum+1}|"
                for row in range(len(board)):
                    rowe += f"{board[colum][row]}|"
                print(rowe)
        def check(x,winner):
            global win
            di_win1 = 0
            di_win2 = 0
            if board[1][1] == x:
                di_win1 += 1
                di_win2 += 1
            if board[0][0] == x:
                di_win1 += 1
            if board[0][2] == x:
                di_win2 += 1
            if board[2][0] == x:
                di_win2 += 1
            if board[2][2] == x:
                di_win1 += 1
            for T_i in range(len(board)):
                ac_win = 0
                dw_win = 0
                for T_j in range(len(board)):
                    if board[T_i][T_j] == x:
                        ac_win += 1
                    else:
                        ac_win = 0
                    if board[T_j][T_i] == x:
                        dw_win += 1
                    else:
                        dw_win = 0
                    if ac_win == 3 or dw_win == 3 or di_win1 == 3 or di_win2 == 3:
                        T_win = True
                        for delete in range(len(available)):
                            available.remove(available[0])
                        return winner
        display_board()
        available = ["1,1","1,2","1,3","2,1","2,2","2,3","3,1","3,2","3,3"]
        playing = True
        turn = randint(0,1)
        while playing:
            if len(available):
                if turn%2:
                    choosing = True
                    choice = input("Your Turn")
                    while choosing:
                        if choice in available:
                            available.remove(choice)
                            choosing = False
                            break
                        else:
                            choice = input("Please enter a valid choice")
                    choice = choice.split(",")
                    board[int (choice[1])-1][int(choice[0])-1] = "X"
                    turn += 1
                    display_board()
                    winner = check("X", "Win")
                else:
                    if len(available):
                        choice = available[randint(0,len(available)-1)]
                        available.remove(choice)
                        choice = choice.split(",")
                        board[int(choice[1])-1][int(choice[0])-1] = "O"
                        turn += 1
                        display_board()
                        winner = check("O", "Lose")
            else:
                playing = False
        if T_win:
            print(f"You {winner}")
        else: 
            print("It's a draw")