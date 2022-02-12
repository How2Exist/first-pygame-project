import pygame
import random

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

image = pygame.image.load("resources/Black_Square.png")

wall_rects = []
wall_images = []

def add_wall_rect(x, y, w, h):
    wall_rects.append([x, y, w, h])
    new_wall_img = pygame.transform.scale(image, (w, h))
    wall_images.append(new_wall_img)

player_rect = [400, 500, 30, 30]
move_speed = 0.1

player_image = pygame.transform.scale(image, (player_rect[RECTATTRW], player_rect[RECTATTRH]))

move_dir_x = 0
move_dir_y = 0

def is_colliding(rect1, rect2):
    if rect1[RECTATTRX] + rect1[RECTATTRW] >= rect2[RECTATTRX] and rect1[RECTATTRX] <= rect2[RECTATTRX] + rect2[RECTATTRW]:
        if rect1[RECTATTRY] + rect1[RECTATTRH] >= rect2[RECTATTRY] and rect1[RECTATTRY] <= rect2[RECTATTRY] + rect2[RECTATTRH]:
            return True

    return False

def draw_rect(rect, image):
    screen.blit(image, (rect[RECTATTRX], rect[RECTATTRY]))

def draw_walls():
    for i in range (len(wall_rects)):
        draw_rect(wall_rects[i], wall_images[i])

game_running = True

add_wall_rect(200, 300, 10, 400)
add_wall_rect(500, 200, 10, 400)

def update_player():
    global game_running
    global move_dir_x
    global move_dir_y
    global player_rect

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    move_dir_x = 0
    move_dir_y = 0

    if keys [pygame.K_w]:
        player_rect[RECTATTRY] -= move_speed
        move_dir_y -= 1

    if keys [pygame.K_s]:
        player_rect[RECTATTRY] += move_speed
        move_dir_y += 1

    if keys [pygame.K_a]:
        player_rect[RECTATTRX] -= move_speed
        move_dir_x -= 1

    if keys [pygame.K_d]:
        player_rect[RECTATTRX] += move_speed
        move_dir_x += 1

while game_running:
    update_player()

#    if (is_colliding(player_rect, wall_rect)):
#        if move_dir_y < 0:
#            player_rect[RECTATTRY] += move_speed
#        if move_dir_y > 0:
#            player_rect[RECTATTRY] -= move_speed
#        if move_dir_x < 0:
#            player_rect[RECTATTRX] += move_speed
#        if move_dir_x > 0:
#            player_rect[RECTATTRX] -= move_speed

    screen.fill((255, 255, 255))

    draw_rect(player_rect, player_image)
    draw_walls()

    pygame.display.update()

