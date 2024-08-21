import pygame
from random import randint, choice
pygame.init()
canvas = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) 
canvas_rect = canvas.get_rect()
w_canvas = canvas_rect.right
h_canvas = canvas_rect.bottom
clock = pygame.time.Clock()
pygame.display.set_caption("Black Jack")
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
def draw(img, rect):
    canvas.blit(img, rect)
game_mode = "Black Jack"
cards = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
suits = ["clubs","diamonds","hearts","spades"]
#suit_num.png (242 × 340)
if True:
    if game_mode == "Black Jack":
        pass
        while game_mode == "Black Jack":
            window("dark green")
            canvas.blit(pygame.transform.scale(pygame.image.load(f"Playing_cards/{choice(suits)}_{choice(cards)}.png"), (121, 170)), (0,0))
            draw(pygame.image.load(f"Playing_cards/{choice(suits)}_{choice(cards)}.png"), pygame.Rect(500,300,242,340))
            pygame.display.update()
            clock.tick(60)
