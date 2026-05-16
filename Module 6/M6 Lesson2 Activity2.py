import pygame

pygame.init()

width, height = 600, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shapes and Colors Lab")

MIDNIGHT_BLUE = (25, 25, 112)
NEON_PINK = (255, 20, 147)
GOLD = (255, 215, 0)
CYAN = (0, 255, 255)

window.fill(MIDNIGHT_BLUE)

pygame.draw.rect(window, NEON_PINK, (225, 150, 150, 100), 5)

triangle_points = [(300, 50), (250, 120), (350, 120)]
pygame.draw.polygon(window, GOLD, triangle_points)

pygame.draw.line(window, CYAN, (0, 0), (600, 400), 2)

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()