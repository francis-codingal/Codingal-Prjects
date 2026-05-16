import pygame

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("My first game screen")

bg_color = (58, 58, 58)

try:
    original_image = pygame.image.load("Little Penguin.png")
    game_image = pygame.transform.scale(original_image, (300, 300))
    image_rect = game_image.get_rect(center=(screen_width // 2, screen_height // 2))
except pygame.error:
    game_image = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(bg_color)

    if game_image:
        screen.blit(game_image, image_rect)

    pygame.display.flip()

pygame.quit()