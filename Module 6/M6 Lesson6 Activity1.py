import math
import random
import pygame

# Using the filenames you provided
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_WIDTH = 48
PLAYER_HEIGHT = 48
ENEMY_WIDTH = 48
ENEMY_HEIGHT = 48
BULLET_WIDTH = 24
BULLET_HEIGHT = 24
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
PLAYER_SPEED = 3
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Ensure these files exist in your folder!
background = pygame.image.load('Space Background.png')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('Space Ship.png')
icon = pygame.transform.scale(icon, (32, 32))
pygame.display.set_icon(icon)

playerImg = pygame.image.load('Shooter.png')
playerImg = pygame.transform.scale(playerImg, (PLAYER_WIDTH, PLAYER_HEIGHT))
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for _i in range(num_of_enemies):
    enemy = pygame.image.load('Space Ship.png')
    enemy = pygame.transform.scale(enemy, (ENEMY_WIDTH, ENEMY_HEIGHT))
    enemyImg.append(enemy)
    enemyX.append(random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

bulletImg = pygame.image.load('missile.png')
bulletImg = pygame.transform.scale(bulletImg, (BULLET_WIDTH, BULLET_HEIGHT))
bulletX = 0
bulletY = PLAYER_START_Y
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 64)
RESTART_BUTTON_WIDTH = 220
RESTART_BUTTON_HEIGHT = 50
RESTART_BUTTON_X = (SCREEN_WIDTH - RESTART_BUTTON_WIDTH) // 2
RESTART_BUTTON_Y = 320
BUTTON_COLOR = (0, 200, 0)
BUTTON_HOVER_COLOR = (0, 255, 0)
TEXT_COLOR = (255, 255, 255)
game_over = False

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def draw_restart_button(mouse_pos):
    button_rect = pygame.Rect(RESTART_BUTTON_X, RESTART_BUTTON_Y, RESTART_BUTTON_WIDTH, RESTART_BUTTON_HEIGHT)
    color = BUTTON_HOVER_COLOR if button_rect.collidepoint(mouse_pos) else BUTTON_COLOR
    pygame.draw.rect(screen, color, button_rect)
    button_text = font.render("RESTART", True, TEXT_COLOR)
    text_x = RESTART_BUTTON_X + (RESTART_BUTTON_WIDTH - button_text.get_width()) // 2
    text_y = RESTART_BUTTON_Y + (RESTART_BUTTON_HEIGHT - button_text.get_height()) // 2
    screen.blit(button_text, (text_x, text_y))
    return button_rect

def restart_game():
    global score_value, playerX, playerY, playerX_change, bulletX, bulletY, bullet_state, enemyX, enemyY, enemyX_change, enemyY_change, game_over
    score_value = 0
    playerX = PLAYER_START_X
    playerY = PLAYER_START_Y
    playerX_change = 0
    bulletX = 0
    bulletY = PLAYER_START_Y
    bullet_state = "ready"
    game_over = False
    for i in range(num_of_enemies):
        enemyX[i] = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
        enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
        enemyX_change[i] = ENEMY_SPEED_X
        enemyY_change[i] = ENEMY_SPEED_Y

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            restart_rect = pygame.Rect(RESTART_BUTTON_X, RESTART_BUTTON_Y, RESTART_BUTTON_WIDTH, RESTART_BUTTON_HEIGHT)
            if restart_rect.collidepoint(event.pos):
                restart_game()
        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -PLAYER_SPEED
                if event.key == pygame.K_RIGHT:
                    playerX_change = PLAYER_SPEED
                if event.key == pygame.K_SPACE and bullet_state == "ready":
                    bulletX = playerX
                    bullet_state = "fire"
            if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                playerX_change = 0

    if not game_over:
        playerX += playerX_change
        playerX = max(0, min(playerX, SCREEN_WIDTH - PLAYER_WIDTH))

        for i in range(num_of_enemies):
            if enemyY[i] > 340:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                playerX_change = 0
                game_over = True
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - ENEMY_WIDTH:
                enemyX_change[i] *= -1
                enemyY[i] += enemyY_change[i]

            if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
                bulletY = PLAYER_START_Y
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
                enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

            screen.blit(enemyImg[i], (enemyX[i], enemyY[i]))
    else:
        game_over_text()
        draw_restart_button(mouse_pos)

    if not game_over:
        if bulletY <= 0:
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
        elif bullet_state == "fire":
            screen.blit(bulletImg, (bulletX + (PLAYER_WIDTH - BULLET_WIDTH) // 2, bulletY + 10))
            bulletY -= BULLET_SPEED_Y

    screen.blit(playerImg, (playerX, playerY))
    show_score(10, 10)
    pygame.display.update()

pygame.quit()