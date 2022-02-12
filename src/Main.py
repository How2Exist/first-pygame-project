import pygame

pygame.init()

screen = pygame.display.set_mode((900 , 600))
pygame.display.set_caption("!¡||⊣ᔑᒲᒷ.ℸ ̣ ᒷᓭℸ ̣.ʖꖎ𝙹ᓵꖌ.⊣ᔑᒲᒷ")
icon = pygame.image.load("resources/MEGASHIP_FIELD (1).jpg")
pygame.display.set_icon(icon)

# rect attrs: [x, y, w, h] as list

RECTATTRX = 0
RECTATTRY = 1
RECTATTRW = 2
RECTATTRH = 3

wall_rect = [600, 300, 40, 40]

player_rect = [400, 500, 30, 30]
move_speed = 0.1

image = pygame.image.load("resources/Black_Square.png")
player_image = pygame.transform.scale(image, (player_rect[RECTATTRW], player_rect[RECTATTRH]))
wall_image = pygame.transform.scale(image, (wall_rect[RECTATTRW], wall_rect[RECTATTRH]))

def is_colliding(rect1, rect2):
    if rect1[RECTATTRX] + rect1[RECTATTRW] >= rect2[RECTATTRX] and rect1[RECTATTRX] <= rect2[RECTATTRX] + rect2[RECTATTRW]:
        if rect1[RECTATTRY] + rect1[RECTATTRH] >= rect2[RECTATTRY] and rect1[RECTATTRY] <= rect2[RECTATTRY] + rect2[RECTATTRH]:
            return True

    return False

def draw_rect(rect, image):
    screen.blit(image, (rect[RECTATTRX], rect[RECTATTRY]))

game_running = True

def update_player():
    global game_running
    global player_rect

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    if keys [pygame.K_w]:
        player_rect[RECTATTRY] -= move_speed

    if keys [pygame.K_s]:
        player_rect[RECTATTRY] += move_speed

    if keys [pygame.K_a]:
        player_rect[RECTATTRX] -= move_speed

    if keys [pygame.K_d]:
        player_rect[RECTATTRX] += move_speed

while game_running:
    update_player()

    if (is_colliding(player_rect, wall_rect)):
        print("collision")

    screen.fill((255, 255, 255))

    draw_rect(player_rect, player_image)
    draw_rect(wall_rect, wall_image)

    pygame.display.update()

















#import random
#words = ["Steam", "Brightchamps", "supercalifragilisticexpialidocious", "pneumonoultramicroscopicsilicovolcanoconiosis"]
#word = random.choice (words)
#name = str(input("Please enter your name: "))
#guessletter = ""
#chances = 10
#print ("Ok, lets start guessing")

#while chances > 0:
#    print ("Guess a letter of the word")
#    guess = input()
#    guessletter += guess
#    wrong = 0
#    for i in word:
#        if i in guessletter:
#            print (i)
#        else:
#            print ("-")
#            wrong = 1






