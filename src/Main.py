import pygame

pygame.init()

screen = pygame.display.set_mode((900 , 600))
pygame.display.set_caption("!¡||⊣ᔑᒲᒷ.ℸ ̣ ᒷᓭℸ ̣.ʖꖎ𝙹ᓵꖌ.⊣ᔑᒲᒷ")
icon = pygame.image.load("resources/MEGASHIP_FIELD (1).jpg")
pygame.display.set_icon(icon)

image = pygame.image.load("resources/Black_Square.png")
imageX = 400
imageY = 500
Image = pygame.transform.scale(image, (60, 60))

def show_image():
    screen.blit(Image, (imageX, imageY))

game_running = True

def update_player():
    global game_running
    global imageX
    global imageY

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    if keys [pygame.K_w]:
        imageY -= 0.1
    if keys [pygame.K_s]:
        imageY += 0.1
    if keys [pygame.K_a]:
        imageX -= 0.1
    if keys [pygame.K_d]:
        imageX += 0.1

while game_running:
    update_player()

    screen.fill((255, 255, 255))
    show_image()
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






