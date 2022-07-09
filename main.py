import pygame
import math
import random

#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 640))

#background
background = pygame.image.load('background.png')


#Title and Icon
pygame.display.set_caption("Tugas UTS")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('dragon (1).png')
playerX = 380
playerY = 520
playerX_change = 0

#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('dragon (2).png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(32)

#Bullet
bulletImg = pygame.image.load('fire.png')
bulletX = 0
bulletY = 520
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"
#ready = You can't see the bullet on the screen
#fire = the bullet is currently moving

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 25)

textX = 10
textY = 10

#game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("Game Over ", True, (255, 255, 255))
    screen.blit(over_text, (200, 290))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemeyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemeyX-bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
#Game Loop
running = True
while running:
    #warna screen
    screen.fill((100,40,75))
    #background image
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #if key is pressed whether is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 4.5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    #get the current x coordinate of the dragon
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

#boundaries biar kaga keluar layar
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

#enemy movement
    for i in range(num_of_enemies):

        #game over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 520
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    #bullet Movement
    #to make multiple bullet
    if bulletY <= 0:
        bulletY = 520
        bullet_state = "ready"
    #to shoot
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    #https: // www.youtube.
