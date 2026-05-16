import pygame

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('My first game screen')

WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
BLACK = (0, 0, 0)

rect_width, rect_height = 150, 80
rect_x = (screen_width // 2) - (rect_width // 2)
rect_y = (screen_height // 2) - (rect_height // 2)

font = pygame.font.SysFont("Arial", 36)
text_surface = font.render("Hello Pygame!", True, BLACK)
text_rect = text_surface.get_rect(center=(screen_width // 2, 50))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    
    pygame.draw.rect(screen, PURPLE, (rect_x, rect_y, rect_width, rect_height))
    
    screen.blit(text_surface, text_rect)

    pygame.display.flip()

pygame.quit()