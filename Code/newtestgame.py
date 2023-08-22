import pygame
from random import randint
pygame.init()
master = True
page = True
exit = True
skin_selection = False
Open_ui = True
winning = False
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

def text(text, a, b, si, col, font):
    font= pygame.font.SysFont(font,si)
    texting = font.render(text, True, col)
    canvas.blit(texting, (a,b))


pj1 = juump(1, 10, False)
pj2 = juump(1, 10, False)
pj3 = juump(1, 10, False)
pj4 = juump(1, 10, False)

rot = 0
rotation = 0

black_bar = pygame.Rect(0,0,1500,120)
startrect = pygame.Rect(1200,800,200,100)
exitrect = pygame.Rect(200,750,150,150)
menurect = pygame.Rect(675,750,150,150)
playagainrect = pygame.Rect(1150,750,150,150)
playrect = pygame.Rect(600,350,300,300)
settingsrect = pygame.Rect(100,750,150,150)
skinrect = pygame.Rect(1250,750,150,150)
gamerect = pygame.Rect(350,425,150,150)
pointselect50 = pygame.Rect(200,800,100,100)
pointselect100 = pygame.Rect(400,800,100,100)
pointselect150 = pygame.Rect(600,800,100,100)
pointselect200 = pygame.Rect(800,800,100,100)
pointselectRnd = pygame.Rect(1000,800,100,100)
dicerect = pygame.Rect(1005,805,100,100)
       
monkeyskin = pygame.Rect(250, 250, 150, 150)
frogskin = pygame.Rect(500, 250, 150, 150)
swskin = pygame.Rect(750, 250, 150, 150)
primeskin = pygame.Rect(1000, 250, 150, 150)

def Skin(sken):
    global player1img
    global player2img
    global player3img
    global player4img
    global yellowe
    global blacke
    global bluee
    if sken == "menkey":
        player1img = pygame.image.load("monkeman21.png")
        player2img = pygame.image.load("monkeman1.png")
        player3img = pygame.image.load("monkey3.png")
        player4img = pygame.image.load("monkey4.png")
        yellowe = pygame.image.load("banan.png")
        blacke = pygame.image.load("brownbanan.png")
        bluee = pygame.image.load("greenbanan.png")
    elif sken == "freg":
        player1img = pygame.image.load("frog1.png")
        player2img = pygame.image.load("frog2.png")
        player3img = pygame.image.load("frog3.png")
        player4img = pygame.image.load("frog4.png")
        yellowe = pygame.image.load("fly.png")
        blacke = pygame.image.load("wasp.png")
        bluee = pygame.image.load("dragonfly.png")
    elif sken == "sw":
        player1img = pygame.image.load("luke.png")
        player2img = pygame.image.load("obiobi.png")
        player3img = pygame.image.load("ahsoka.png")
        player4img = pygame.image.load("seagulls.png")

player1 = pygame.Rect(125, deck, 150, 147)
player2 = pygame.Rect(500, deck, 150, 147)
player3 = pygame.Rect(875, deck, 150, 147)
player4 = pygame.Rect(1250, deck, 150, 147)
start_player1 = pygame.Rect(200, 200, 150, 147)
start_player2 = pygame.Rect(1050, 200, 150, 147)
start_player3 = pygame.Rect(200, 500, 150, 147)
start_player4 = pygame.Rect(1050, 500, 150, 147)
backrect = pygame.Rect(75,75,100,100)
primary = True


try:
    monkeyselect = pygame.image.load("monkeman21.png")
    frogselect = pygame.image.load("frog1.png")
    swselect = pygame.image.load("luke.png")
    sky = pygame.image.load("sky1.jpg")
    sky = pygame.transform.scale(sky, (1500, 1200))
    grass = pygame.image.load("grass1.jpg")
    grass = pygame.transform.scale(grass, (1500, 300))
    start = pygame.image.load("start.png")
    exiticon = pygame.image.load("exiticon.png")
    menu = pygame.image.load("menu.png")
    playagain = pygame.image.load("playagain.png")
    playbutton = pygame.image.load("playbutton.png")
    Skin("menkey")
    skin = pygame.image.load("skin.png")
    settings = pygame.image.load("settings.png")
    gamebutton = pygame.image.load("gameicon.png")
    backarrow = pygame.image.load("Arrow.png")
    dice = pygame.image.load("dice.png")
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
    gamebutton = black
    primary = False
    def draw(img, rect):
        return pygame.draw.rect(canvas, img, rect)

def rotate(img, rect, angle):
    rotated_img = pygame.transform.rotozoom(img, angle, 1)
    canvas.blit(rotated_img, rotated_img.get_rect(center=img.get_rect(topleft=(rect.x, rect.y)).center).topleft)

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
    global orangei5
    orangei1 = orange
    orangei2 = orange
    orangei3 = orange
    orangei4 = orange
    orangei5 = orange

T_p1score = 0
T_p2score = 0
T_11 = pygame.Rect(250,0,300,300)
T_12 = pygame.Rect(250,350,300,300)
T_13 = pygame.Rect(250,700,300,300)
T_21 = pygame.Rect(600,0,300,300)
T_22 = pygame.Rect(600,350,300,300)
T_23 = pygame.Rect(600,700,300,300)
T_31 = pygame.Rect(950,0,300,300)
T_32 = pygame.Rect(950,350,300,300)
T_33 = pygame.Rect(950,700,300,300)
T_exitrect = pygame.Rect(1300,750,300,300)
T_menurect = pygame.Rect(50,750,300,300)

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
        draw(gamebutton, gamerect)
        if primary:
            draw(skin, skinrect)
        #draw(settings, settingsrect)
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()[0]
        mousepos = pygame.mouse.get_pos()
        if mouse or keys[pygame.K_RETURN]:
            if playrect.collidepoint(mousepos) or keys[pygame.K_RETURN]:
                    Open_ui = False
                    page = False
        if mouse:
            if gamerect.collidepoint(mousepos):
                page = False
                Tic_Tac_Toe = True
        if primary:
            if mouse:
                if skinrect.collidepoint(mousepos):
                    page = False
                    skin_selection = True
        if keys[pygame.K_q] and keys[pygame.K_p]:
            pygame.quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update() 

    while skin_selection:
        canvas.fill(white)
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()[0]
        mousepos = pygame.mouse.get_pos()
        text("Skin Selection", 250, 50, 200, black, "jungle adventurer")
        draw(monkeyselect, monkeyskin)
        text("Monkey", 250, 400, 50, black, "jungle adventurer")
        draw(frogselect, frogskin)
        text("Frog", 500, 400, 50, black, "jungle adventurer")
        draw(swselect, swskin)
        text("Star Wars", 750, 400, 50, black, "jungle adventurer")
        draw(player4img, primeskin)
        text("Waldon", 1000, 400, 50, black, "jungle adventurer")
        draw(menu, menurect)
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
        if mouse:
            if monkeyskin.collidepoint(mousepos):
                Skin("menkey")
            if frogskin.collidepoint(mousepos):
                Skin("freg")
            if swskin.collidepoint(mousepos):
                Skin("sw")
            if menurect.collidepoint(mousepos):
                page = True
                skin_selection = False
        if keys[pygame.K_q] and keys[pygame.K_p]:
            pygame.quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update() 

    while not Open_ui:
        canvas.fill(black)
        text(f"Win points = {winpoints}", 500, 100, 100, white, "arial")
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
        draw(player1img, start_player1)
        draw(player2img, start_player2)
        draw(player3img, start_player3)
        draw(player4img, start_player4)
        draw(backarrow, backrect)
        if winpoints == 0:
            resetorangei()
        elif winpoints == 50:
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
            orangei5 = green
        pygame.draw.rect(canvas, orangei1, pointselect50)
        pygame.draw.rect(canvas, orangei2, pointselect100)
        pygame.draw.rect(canvas, orangei3, pointselect150)
        pygame.draw.rect(canvas, orangei4, pointselect200)
        pygame.draw.rect(canvas, orangei5, pointselectRnd)
        text("50", 225, 825, 50, black, "arial")
        text("100", 412.5, 825, 50, black, "arial")
        text("150", 612.5, 825, 50, black, "arial")
        text("200", 812.5, 825, 50, black, "arial")
        if primary:
            draw(dice, dicerect)
        else:
            text("Rnd", 1012.5, 825, 50, black, "arial")
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
            if pointselectRnd.collidepoint(mousepos):
                winpoints = randint(50, 200)
                pygame.time.delay(100)
            if backrect.collidepoint(mousepos):
                page = True
                Open_ui = True
        if  keys[pygame.K_5]:
            winpoints = 50
            pygame.time.delay(100)
        if keys[pygame.K_6]:
            winpoints = 100
            pygame.time.delay(100)
        if keys[pygame.K_7]:
            winpoints = 150
            pygame.time.delay(100)
        if keys[pygame.K_8]:
            winpoints = 200
            pygame.time.delay(100)
        if keys[pygame.K_9]:
            winpoints = randint(50, 200)
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
            text("Player 1 is playing",100,350,50,green, "arial")
        else:
            text("Player 1 is not playing",100,350,50,red, "arial")
        if isplay2%2:
            text("Player 2 is playing",950,350,50,green, "arial")
        else:
            text("Player 2 is not playing",950,350,50,red, "arial")
        if isplay3%2:
            text("Player 3 is playing",100,650,50,green, "arial")
        else:
            text("Player 3 is not playing",100,650,50,red, "arial")
        if isplay4%2:
            text("Player 4 is playing",950,650,50,green, "arial")
        else:
            text("Player 4 is not playing",950,650,50,red, "arial")
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
        rot += 1
        rotate(banana1.picture, Banana_rect1, rot)
        rotate(banana2.picture, Banana_rect2, rot)
        rotate(banana3.picture, Banana_rect3, rot)
        rotate(banana4.picture, Banana_rect4, rot)
        rotate(banana5.picture, Banana_rect5, rot)
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
        pygame.draw.rect(canvas, black, black_bar)
        if isplay1%2:
            text("Player 1: "+str(p1points),40,60,60,white, "Jungle Adventurer")
        if isplay2%2:
            text("Player 2: "+str(p2points),300,60,60,white, "Jungle Adventurer")
        if isplay3%2:
            text("Player 3: "+str(p3points),950,60,60,white, "Jungle Adventurer")
        if isplay4%2:
            text("Player 4: "+str(p4points),1200,60,60,white, "Jungle Adventurer")
        text("Goal: "+str(winpoints),600,50,100,white,"Jungle Adventurer")
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
        text(f"{winner} is Full",200,300,200,black, "arial")
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
                winpoints = 0
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
        pygame.time.delay(100)
        T_break = False
        canvas.fill(white)
        pygame.draw.rect(canvas, white, (250,0,1000,1000))
        pygame.draw.rect(canvas, black, (250,300,1000,50))
        pygame.draw.rect(canvas, black, (250,650,1000,50))
        pygame.draw.rect(canvas, black, (550,0,50,1000))
        pygame.draw.rect(canvas, black, (900,0,50,1000))
        draw(exiticon, T_exitrect)
        draw(menu, T_menurect)
        text(str(T_p1score), 125,125,125,black,"Jungle Adventurer")
        text(str(T_p2score), 1375,125,125,black,"Jungle Adventurer")
        mouse = pygame.mouse.get_pressed()[0]
        mousepos = pygame.mouse.get_pos()
        board = [[" "," ", " "],[" "," "," "],[" "," "," "]]
        T_win = False
        def edit_T_board(who,placement1,placement2): 
            if placement1 == "1":
                ab = 325
            if placement1 == "2":
                ab = 675
            if placement1 == "3":
                ab = 1025
            if placement2 == "1":
                ba = 100
            if placement2 == "2":
                ba = 425
            if placement2 == "3":
                ba = 750
            if primary:
                if who == "X":
                    T_img = player1img
                else:
                    T_img = player2img
                canvas.blit(T_img, (ab,ba))
            else:
                text(who, (ab-25), (ba-100), 300, black, "arial")
        def check(x,winner):
            global T_win
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
        available = ["1,1","1,2","1,3","2,1","2,2","2,3","3,1","3,2","3,3"]
        playing = True
        turn = randint(0,1)
        while playing:
            pygame.time.delay(100)
            if len(available):
                if turn%2:
                    choosing = True
                    while choosing:
                        mouse = pygame.mouse.get_pressed()[0]
                        mousepos = pygame.mouse.get_pos()
                        if mouse:
                            choice = 0
                            if T_11.collidepoint(mousepos):
                                choice = "1,1"
                            if T_12.collidepoint(mousepos):
                                choice = "1,2"
                            if T_13.collidepoint(mousepos):
                                choice = "1,3"
                            if T_21.collidepoint(mousepos):
                                choice = "2,1"
                            if T_22.collidepoint(mousepos):
                                choice = "2,2"
                            if T_23.collidepoint(mousepos):
                                choice = "2,3"
                            if T_31.collidepoint(mousepos):
                                choice = "3,1"
                            if T_32.collidepoint(mousepos):
                                choice = "3,2"
                            if T_33.collidepoint(mousepos):
                                choice = "3,3"
                            if T_exitrect.collidepoint(mousepos):
                                pygame.quit()
                            if T_menurect.collidepoint(mousepos):
                                page = True
                                Tic_Tac_Toe = False
                                choosing = False
                                playing = False
                                T_break = True
                                T_p1score = 0
                                T_p2score = 0
                        if choice in available:
                            available.remove(choice)
                            choosing = False
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_q] and keys[pygame.K_p]:
                            pygame.quit()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                        pygame.display.update()
                        clock.tick(600)
                    if not T_break:
                        choice = choice.split(",")
                        edit_T_board("X",choice[0],choice[1])
                        board[int (choice[1])-1][int(choice[0])-1] = "X"
                        turn += 1
                        winner = check("X", "Win")
                else:
                    if len(available):
                        choice = available[randint(0,len(available)-1)]
                        available.remove(choice)
                        choice = choice.split(",")
                        board[int(choice[1])-1][int(choice[0])-1] = "O"
                        edit_T_board("O",choice[0],choice[1])
                        turn += 1
                        winner = check("O", "Lose")
            else:
                playing = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q] and keys[pygame.K_p]:
                pygame.quit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            pygame.display.update()
            clock.tick(600)

        if T_win:
            if winner == "Win":
                T_p1score += 1
            else:
                T_p2score += 1
        else: 
            pass
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] and keys[pygame.K_p]:
            pygame.quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
        clock.tick(600)

